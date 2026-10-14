function toggleMenu(button){
  const menu = document.querySelector('.links');
  if(!menu) return;
  const open = menu.classList.toggle('open');
  if(button) button.setAttribute('aria-expanded', String(open));
}

const TERRAMORPH_PHONE_NUMBER = '4198736801';
const TERRAMORPH_PHONE_HREF = `tel:${TERRAMORPH_PHONE_NUMBER}`;
const TERRAMORPH_PHONE_DISPLAY = '419-873-6801';
const TRACKING_STORAGE_KEY = 'terramorphAttributionContext';
const QUICK_LEAD_KEY = 'terramorphQuickLeadContext';
const PHONE_LEAD_KEY = 'terramorphPendingPhoneLead';
const THANK_YOU_ATTRIBUTION_KEY = 'terramorphThankYouLeadTracked';
const JOBBER_ORIGIN = 'https://clienthub.getjobber.com';
const JOBBER_LEAD_TRACKED_KEY = 'terramorphJobberLeadTracked';
// Google Ads "Request quote" conversion label (the part after AW-17691366114/).
// Blank skips the direct Google Ads conversion ping.
const AW_QUOTE_REQUEST_LABEL = 'obvlCJaFougcEOKl8_NB';
const QUOTE_POPUP_DISMISS_KEY = 'terramorphQuotePopupDismissedAt';
const QUOTE_POPUP_DISMISS_MS = 14 * 24 * 60 * 60 * 1000;
const QUOTE_POPUP_MIN_DELAY_MS = 45 * 1000;
const QUOTE_POPUP_FALLBACK_MS = 90 * 1000;
const META_SOURCES = new Set(['facebook', 'instagram', 'meta', 'fb', 'ig']);
const TRACKING_PARAM_KEYS = [
  'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term',
  'fb_campaign_id', 'fb_adset_id', 'fb_ad_id', 'fb_placement',
  'fbclid', 'gclid', 'wbraid', 'gbraid', 'msclkid'
];
let quotePopupReturnFocus = null;

function getDetectedTrafficSource(){
  const params = new URLSearchParams(window.location.search);
  const directSource = (params.get('utm_source') || params.get('source') || '').toLowerCase();
  if(directSource) return directSource;
  const ref = document.referrer.toLowerCase();
  if(ref.includes('facebook.com') || ref.includes('fb.com')) return 'facebook';
  if(ref.includes('instagram.com')) return 'instagram';
  if(ref.includes('google.')) return 'google';
  return '';
}

function readStoredJson(key){
  try {
    const raw = window.localStorage?.getItem(key);
    return raw ? JSON.parse(raw) : null;
  } catch(error) {
    console.warn('Storage read failed', key, error);
    return null;
  }
}

function writeStoredJson(key, value){
  try {
    window.localStorage?.setItem(key, JSON.stringify(value));
  } catch(error) {
    console.warn('Storage write failed', key, error);
  }
}

function getCookieValue(name){
  const escaped = name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const match = document.cookie.match(new RegExp('(?:^|; )' + escaped + '=([^;]*)'));
  return match ? decodeURIComponent(match[1]) : '';
}

function getFbcFromFbclid(fbclid){
  if(!fbclid) return '';
  return `fb.1.${Math.floor(Date.now() / 1000)}.${fbclid}`;
}

function getCurrentTrackingParams(){
  const params = new URLSearchParams(window.location.search);
  const context = {};
  TRACKING_PARAM_KEYS.forEach(key => {
    const value = params.get(key);
    if(value) context[key] = value;
  });
  if(!context.utm_source){
    const detectedSource = getDetectedTrafficSource();
    if(detectedSource) context.utm_source = detectedSource;
  }
  if(!context.utm_medium && document.querySelector('[data-funnel-service]') && context.utm_source){
    context.utm_medium = 'paid_social';
  }
  const fbp = getCookieValue('_fbp');
  const fbc = getCookieValue('_fbc') || getFbcFromFbclid(context.fbclid);
  if(fbp) context.fbp = fbp;
  if(fbc) context.fbc = fbc;
  context.landing_page = window.location.pathname;
  context.landing_url = window.location.href;
  context.landing_title = document.title;
  const funnelService = document.querySelector('[data-funnel-service]')?.dataset.funnelService || document.querySelector('[data-service]')?.dataset.service || '';
  if(funnelService) context.service_category = funnelService;
  return context;
}

function persistTrackingContext(){
  const current = getCurrentTrackingParams();
  const existing = readStoredJson(TRACKING_STORAGE_KEY) || {};
  const merged = {
    ...existing,
    ...Object.fromEntries(Object.entries(current).filter(([, value]) => value)),
    first_touch_at: existing.first_touch_at || new Date().toISOString(),
    last_touch_at: new Date().toISOString()
  };
  writeStoredJson(TRACKING_STORAGE_KEY, merged);
  return merged;
}

function getStoredTrackingContext(){
  return readStoredJson(TRACKING_STORAGE_KEY) || {};
}

function getMergedTrackingContext(){
  return {
    ...getStoredTrackingContext(),
    ...Object.fromEntries(Object.entries(getCurrentTrackingParams()).filter(([, value]) => value))
  };
}

function metaTrack(eventName, parameters = {}, options = {}){
  if(typeof fbq !== 'function') return;
  try {
    if(options.eventId){
      fbq('track', eventName, parameters, {eventID: options.eventId});
    } else {
      fbq('track', eventName, parameters);
    }
  } catch(error) {
    console.warn('Meta Pixel tracking failed', eventName, error);
  }
}

function metaTrackCustom(eventName, parameters = {}){
  if(typeof fbq !== 'function') return;
  try {
    fbq('trackCustom', eventName, parameters);
  } catch(error) {
    console.warn('Meta Pixel custom tracking failed', eventName, error);
  }
}

function pushAnalyticsEvent(eventName, context = {}){
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({event: eventName, ...context});

  if(typeof gtag === 'function'){
    try {
      const {event, ...ga4Params} = context || {};
      gtag('event', eventName, ga4Params);
    } catch(error) {
      console.warn('GA4 event tracking failed', eventName, error);
    }
  }
}

function getTrackingContext(){
  const stored = getMergedTrackingContext();
  const quickLead = readStoredJson(QUICK_LEAD_KEY) || {};
  const service = document.querySelector('[data-funnel-service]')?.dataset.funnelService || document.querySelector('[data-service]')?.dataset.service || stored.service_category || '';
  return {
    page_title: document.title,
    page_path: window.location.pathname,
    page_url: window.location.href,
    service_category: service || 'general',
    traffic_source: stored.utm_source || getDetectedTrafficSource() || 'direct',
    utm_source: stored.utm_source || '',
    utm_medium: stored.utm_medium || '',
    utm_campaign: stored.utm_campaign || '',
    utm_content: stored.utm_content || '',
    utm_term: stored.utm_term || '',
    fb_campaign_id: stored.fb_campaign_id || '',
    fb_adset_id: stored.fb_adset_id || '',
    fb_ad_id: stored.fb_ad_id || '',
    fb_placement: stored.fb_placement || '',
    fbclid: stored.fbclid || '',
    gclid: stored.gclid || '',
    wbraid: stored.wbraid || '',
    gbraid: stored.gbraid || '',
    msclkid: stored.msclkid || '',
    fbp: stored.fbp || getCookieValue('_fbp') || '',
    fbc: stored.fbc || getCookieValue('_fbc') || getFbcFromFbclid(stored.fbclid) || '',
    lead_service: quickLead.service || '',
    lead_city: quickLead.city || '',
    lead_timeline: quickLead.timeline || ''
  };
}

function decorateTrackingLink(link){
  const href = link?.getAttribute('href') || '';
  if(!href || href.startsWith('#')) return;
  let destination;
  try {
    destination = new URL(href, window.location.href);
  } catch(error) {
    console.warn('Tracking link could not be parsed', href, error);
    return;
  }
  const isTerramorphLink = destination.origin === window.location.origin;
  const isJobberLink = destination.hostname === 'clienthub.getjobber.com';
  if(!isTerramorphLink && !isJobberLink) return;
  const context = getMergedTrackingContext();
  TRACKING_PARAM_KEYS.forEach(key => {
    const value = context[key];
    if(value && !destination.searchParams.has(key)) destination.searchParams.set(key, value);
  });
  link.setAttribute('href', destination.toString());
}

function decorateAttributionLinks(){
  document.querySelectorAll('a[href*="quote.html"], a[href*="clienthub.getjobber.com"]').forEach(decorateTrackingLink);
}

function trackQuoteIntent(source, link){
  const context = {
    source: source || 'quote',
    destination_url: link?.href || '',
    ...getTrackingContext()
  };
  pushAnalyticsEvent('quote_intent', context);
  metaTrack('Contact', {content_name: 'Terramorph quote intent', content_category: context.source, lead_stage: 'intent', ...context});
  metaTrackCustom('QuoteIntent', context);
}

function hasMetaAttribution(context){
  const normalizedSource = String(context.utm_source || '').trim().toLowerCase();
  return normalizedSource
    ? META_SOURCES.has(normalizedSource)
    : Boolean(context.fbclid || context.fbc || context.fb_campaign_id || context.fb_adset_id || context.fb_ad_id);
}

function trackPhoneClick(link){
  const context = {source: 'phone_click', phone_number: (link?.getAttribute('href') || '').replace(/^tel:/, ''), ...getTrackingContext()};
  pushAnalyticsEvent('phone_click', context);
  metaTrack('Contact', {content_name: 'Terramorph phone click', content_category: 'phone_call', ...context});
  metaTrackCustom('PhoneClick', context);
}

const JOBBER_HOSTED_FORM_URL = 'https://clienthub.getjobber.com/hubs/e644a784-b214-4a2b-93df-ace28dbb2a70/public/requests/1578803/new';

// True only when the visitor actually clicked a paid ad. Deliberately does NOT
// trust utm_source alone: getDetectedTrafficSource() infers that from
// document.referrer, so an organic Facebook post click would look paid here.
function hasPaidClickAttribution(context){
  const medium = String(context.utm_medium || '').trim().toLowerCase();
  return Boolean(
    context.fbclid || context.fb_ad_id || context.fb_campaign_id ||
    context.gclid || context.wbraid || context.gbraid || context.msclkid ||
    medium === 'paid' || medium === 'cpc' || medium === 'ppc' || medium === 'paid_social'
  );
}

// Jobber's EMBED is a cross-origin iframe. Jobber states in the form settings
// that "custom confirmation pages won't work in embedded forms", so a
// submission inside it can never redirect and can only ever be guessed at from
// iframe load/height signals -- which is why Meta under-reported form leads
// about 4x (1 counted vs 4 self-reported in Jobber, Oct 5-11 2026).
//
// For paid clicks only, swap the embed for the HOSTED form. It redirects to
// /thank-you.html on submit, where trackAttributedThankYouView() fires exactly
// one Meta Lead and one Google Ads conversion per real submission. Organic
// visitors keep the inline embed, so their experience is unchanged.
function routePaidTrafficToHostedForm(){
  const panels = document.querySelectorAll('.jobber-quote-panel:not([data-request-route])');
  if(!panels.length) return;
  if(!hasPaidClickAttribution(getMergedTrackingContext())) return;
  panels.forEach(panel => {
    const embed = panel.querySelector('.jobber-embed-wrap');
    const fallback = panel.querySelector('.jobber-fallback');
    if(!embed) return;
    const heading = panel.querySelector('h2')?.textContent?.trim() || 'Request My Free Estimate';
    const action = document.createElement('div');
    action.className = 'hosted-request-action';
    action.innerHTML = [
      '<p class="eyebrow">Takes about a minute</p>',
      '<ul class="hosted-request-list">',
      '<li>Your name, phone, and email</li>',
      '<li>Property address and ZIP code</li>',
      '<li>What the project needs and your timeline</li>',
      '<li>Photos of the area, if you have them</li>',
      '</ul>',
      `<a class="btn btn-gold btn-request-primary" href="${JOBBER_HOSTED_FORM_URL}" rel="noopener">${heading}</a>`,
      '<p class="hosted-request-note">Opens Terramorph\'s secure Jobber request form. No account needed.</p>',
      '<p class="hosted-request-or">Would rather talk it through?</p>',
      `<a class="btn btn-request-secondary" href="${TERRAMORPH_PHONE_HREF}">Call ${TERRAMORPH_PHONE_DISPLAY}</a>`
    ].join('');
    embed.replaceWith(action);
    fallback?.remove();
    panel.setAttribute('data-request-route', 'hosted');
  });
}

function trackAttributedThankYouView(){
  if(!(window.location.pathname.endsWith('/thank-you.html') || window.location.pathname.endsWith('/thank-you'))) return;
  if(window.sessionStorage?.getItem(THANK_YOU_ATTRIBUTION_KEY)) return;
  const context = getTrackingContext();
  const hasAttributionContext = Boolean(
    context.fbclid || context.fb_ad_id || context.gclid || context.msclkid ||
    context.utm_source || context.utm_campaign ||
    context.lead_service || context.lead_city || context.lead_timeline
  );
  if(!hasAttributionContext){
    pushAnalyticsEvent('quote_thank_you_view_unattributed', {source: 'thank_you_page_unattributed', ...context});
    return;
  }
  const eventId = `thank-you-${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;
  const attributionContext = {
    source: 'thank_you_page_attributed_diagnostic',
    lead_stage: 'thank_you_return',
    ...context
  };
  // Jobber's native form_submit event is mapped to GA4 generate_lead. This
  // diagnostic must not emit another GA4 lead when the visitor returns here.
  pushAnalyticsEvent('quote_thank_you_attributed', attributionContext);
  // Jobber's HOSTED form (not the embed) redirects here after submission, a
  // path the iframe detector never sees. The Ads action counts one per click,
  // so a double fire with the embed path cannot inflate conversions.
  if(AW_QUOTE_REQUEST_LABEL && typeof gtag === 'function' &&
     (context.gclid || context.wbraid || context.gbraid)){
    try {
      gtag('event', 'conversion', {send_to: `AW-17691366114/${AW_QUOTE_REQUEST_LABEL}`});
    } catch(error) {
      console.warn('Google Ads conversion tracking failed', error);
    }
  }
  const leadContext = {...attributionContext, meta_attributed: hasMetaAttribution(context)};
  metaTrack('Lead', {content_name: 'Terramorph quote request', content_category: context.service_category || 'quote_request', ...leadContext}, {eventId});
  metaTrackCustom('QuoteThankYouAttribution', leadContext);
  window.sessionStorage?.setItem(THANK_YOU_ATTRIBUTION_KEY, eventId);
}

function buildQuickLeadEventId(){
  return `quick-lead-${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;
}

function collectQuickLeadFields(form){
  const data = new FormData(form);
  return {
    name: String(data.get('name') || '').trim(),
    phone: String(data.get('phone') || '').trim(),
    city: String(data.get('city') || '').trim(),
    service: String(data.get('service') || form.dataset.service || getTrackingContext().service_category || '').trim(),
    timeline: String(data.get('timeline') || '').trim(),
    problem: String(data.get('problem') || '').trim()
  };
}


function collectRequestFields(form){
  const data = new FormData(form);
  return {
    name: String(data.get('name') || '').trim(),
    phone: String(data.get('phone') || '').trim(),
    city: String(data.get('city') || '').trim(),
    address: String(data.get('address') || '').trim(),
    service: String(data.get('service') || '').trim(),
    timeline: String(data.get('timeline') || '').trim(),
    problem: String(data.get('problem') || '').trim()
  };
}

function buildRequestMessage(lead){
  return [
    'Terramorph quote request',
    `Name: ${lead.name}`,
    `Phone: ${lead.phone}`,
    `City: ${lead.city}`,
    lead.address ? `Address: ${lead.address}` : '',
    `Service: ${lead.service}`,
    lead.timeline ? `Timeline: ${lead.timeline}` : '',
    `Project details: ${lead.problem}`
  ].filter(Boolean).join('\n');
}

function handleRequestFormSubmit(form, event){
  event.preventDefault();
  const status = form.querySelector('[data-request-status]');
  const button = form.querySelector('[type="submit"]');
  const lead = collectRequestFields(form);
  const missing = [];
  if(!lead.name) missing.push('name');
  if(!lead.phone) missing.push('phone');
  if(!lead.city) missing.push('city');
  if(!lead.service) missing.push('service');
  if(!lead.problem) missing.push('project details');
  if(missing.length){
    if(status) status.textContent = `Add ${missing.join(', ')} before sending the quote request.`;
    form.classList.add('quick-lead-form-error');
    return;
  }

  const eventId = buildQuickLeadEventId();
  const message = buildRequestMessage(lead);
  const storedLead = {
    ...lead,
    message,
    event_id: eventId,
    created_at: new Date().toISOString(),
    source: 'quote_request_form',
    ...getMergedTrackingContext()
  };
  writeStoredJson(QUICK_LEAD_KEY, storedLead);
  writeStoredJson(PHONE_LEAD_KEY, storedLead);
  pushAnalyticsEvent('quote_request_form_submit', {lead_service: lead.service, lead_city: lead.city, lead_timeline: lead.timeline, lead_problem_length: lead.problem.length, ...getTrackingContext()});
  metaTrack('Contact', {content_name: 'Terramorph text request intent', content_category: lead.service || 'quote_request', ...getTrackingContext()});
  metaTrackCustom('QuoteRequestFormSubmit', {lead_service: lead.service, lead_city: lead.city, ...getTrackingContext()});

  if(button){
    button.disabled = true;
    button.textContent = 'Opening text message...';
  }
  if(status){
    status.innerHTML = `Opening a text to Terramorph. If it does not open, copy this message and send it to ${TERRAMORPH_PHONE_DISPLAY}:<br><textarea class="request-copy-box" readonly>${message.replace(/[&<>]/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[ch]))}</textarea>`;
  }
  window.location.href = `sms:${TERRAMORPH_PHONE_NUMBER}?&body=${encodeURIComponent(message)}`;
}

function handleQuickLeadSubmit(form, event){
  event.preventDefault();
  const button = form.querySelector('[type="submit"]');
  const status = form.querySelector('[data-quick-lead-status]');
  const quickLead = collectQuickLeadFields(form);
  const missing = [];
  if(!quickLead.name) missing.push('name');
  if(!quickLead.phone) missing.push('phone');
  if(!quickLead.city) missing.push('city');
  if(!quickLead.problem) missing.push('project details');
  if(missing.length){
    if(status) status.textContent = `Add ${missing.join(', ')} so Terramorph knows what to review.`;
    form.classList.add('quick-lead-form-error');
    return;
  }

  const eventId = buildQuickLeadEventId();
  const context = {
    source: 'paid_landing_quick_form',
    lead_stage: 'quick_form_call_prompt',
    ...getTrackingContext(),
    lead_service: quickLead.service,
    lead_city: quickLead.city,
    lead_timeline: quickLead.timeline,
    lead_problem_length: quickLead.problem.length
  };
  const storedLead = {
    ...quickLead,
    event_id: eventId,
    created_at: new Date().toISOString(),
    destination_url: TERRAMORPH_PHONE_HREF,
    phone_call: true,
    ...getMergedTrackingContext()
  };
  writeStoredJson(QUICK_LEAD_KEY, storedLead);
  writeStoredJson(PHONE_LEAD_KEY, storedLead);
  pushAnalyticsEvent('quick_lead_continue', context);
  metaTrack('Contact', {content_name: 'Terramorph quick quote intent', content_category: quickLead.service || 'paid_landing', ...context});
  metaTrackCustom('QuickLeadContinue', context);
  if(button){
    button.disabled = true;
    button.textContent = `Calling ${TERRAMORPH_PHONE_DISPLAY}...`;
  }
  if(status) status.textContent = `Good - opening your phone so you can call Terramorph at ${TERRAMORPH_PHONE_DISPLAY}.`;
  window.location.href = TERRAMORPH_PHONE_HREF;
}

function fireJobberLeadConversion(detection){
  if(window.sessionStorage?.getItem(JOBBER_LEAD_TRACKED_KEY)) return;
  const eventId = `jobber-lead-${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;
  const context = {
    source: detection.signal,
    lead_stage: 'jobber_form_submitted',
    iframe_load_count: detection.loadCount,
    iframe_max_height: detection.maxHeight,
    iframe_last_height: detection.lastHeight,
    ...getTrackingContext()
  };
  pushAnalyticsEvent('jobber_request_submitted', context);
  if(AW_QUOTE_REQUEST_LABEL && typeof gtag === 'function'){
    try {
      gtag('event', 'conversion', {send_to: `AW-17691366114/${AW_QUOTE_REQUEST_LABEL}`});
    } catch(error) {
      console.warn('Google Ads conversion tracking failed', error);
    }
  }
  // Every submission goes to Meta. Meta does its own click/view matching, so
  // withholding non-Meta submissions starves the optimizer (3 Leads in 28 days
  // as of 2026-09-09) and drops cross-device conversions it could have matched.
  const leadContext = {...context, meta_attributed: hasMetaAttribution(context)};
  metaTrack('Lead', {content_name: 'Terramorph quote request', content_category: context.service_category || 'quote_request', ...leadContext}, {eventId});
  metaTrackCustom('JobberRequestSubmitted', leadContext);
  window.sessionStorage?.setItem(JOBBER_LEAD_TRACKED_KEY, eventId);
  // Shares the thank-you marker so one submission cannot produce a second
  // Meta Lead if Jobber also returns the visitor to thank-you.html.
  window.sessionStorage?.setItem(THANK_YOU_ATTRIBUTION_KEY, eventId);
}

function watchJobberFormSubmission(){
  const wrap = document.querySelector('.jobber-embed-wrap');
  if(!wrap) return;
  const state = {iframe: null, loadCount: 0, firstLoadAt: 0, maxHeight: 0, lastHeight: 0, engaged: false, signaled: {}};

  const signalOnce = (signal, extras) => {
    if(state.signaled[signal]) return;
    state.signaled[signal] = true;
    pushAnalyticsEvent('jobber_iframe_signal', {signal, engaged: state.engaged, ...extras, ...getTrackingContext()});
    if(state.engaged){
      fireJobberLeadConversion({signal, loadCount: state.loadCount, maxHeight: state.maxHeight, lastHeight: state.lastHeight});
    }
  };

  const attach = iframe => {
    if(!iframe || state.iframe === iframe) return;
    state.iframe = iframe;
    iframe.addEventListener('load', () => {
      state.loadCount += 1;
      if(state.loadCount === 1){
        state.firstLoadAt = Date.now();
        return;
      }
      // Jobber's form swaps to its confirmation page in a second iframe
      // navigation; validation errors re-render without navigating.
      signalOnce('iframe_reload', {iframe_load_count: state.loadCount});
    });
  };

  attach(wrap.querySelector('iframe'));
  new MutationObserver(() => attach(wrap.querySelector('iframe'))).observe(wrap, {childList: true, subtree: true});

  // Clicking into the cross-origin iframe blurs the parent window while the
  // iframe becomes the active element - the only visible sign of engagement.
  window.addEventListener('blur', () => {
    if(state.iframe && document.activeElement === state.iframe) state.engaged = true;
  });

  window.addEventListener('message', event => {
    if(event.origin !== JOBBER_ORIGIN || !state.iframe) return;
    const height = typeof event.data === 'string' ? Number.parseInt(event.data, 10) : NaN;
    if(!Number.isFinite(height) || height <= 0) return;
    state.lastHeight = height;
    if(height > state.maxHeight){
      state.maxHeight = height;
      return;
    }
    const collapsed = state.maxHeight > 600 && height < state.maxHeight * 0.45;
    const settled = state.firstLoadAt && Date.now() - state.firstLoadAt > 8000;
    if(collapsed && settled){
      signalOnce('iframe_collapse', {iframe_max_height: state.maxHeight, iframe_last_height: height});
    }
  });
}

function isQuotePopupDismissed(){
  try {
    const dismissedAt = Number(window.localStorage?.getItem(QUOTE_POPUP_DISMISS_KEY));
    if(!Number.isFinite(dismissedAt) || dismissedAt <= 0) return false;
    if(Date.now() - dismissedAt < QUOTE_POPUP_DISMISS_MS) return true;
    window.localStorage?.removeItem(QUOTE_POPUP_DISMISS_KEY);
  } catch(error) {
    console.warn('Popup storage read failed', error);
  }
  return false;
}

function getQuotePopupFocusableElements(popup){
  return Array.from(popup.querySelectorAll('a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'))
    .filter(element => !element.hidden && element.getAttribute('aria-hidden') !== 'true');
}

function openQuotePopup(reason = 'engaged_visit'){
  const popup = document.querySelector('#quote-popup');
  if(!popup || popup.dataset.opened === 'true') return;
  if(document.body.classList.contains('quote-page') || document.querySelector('[data-funnel-service]')) return;
  if(isQuotePopupDismissed()) return;
  const form = document.querySelector('#request-form');
  const formRect = form?.getBoundingClientRect();
  if(formRect && formRect.top < window.innerHeight && formRect.bottom > 0) return;
  quotePopupReturnFocus = document.activeElement instanceof HTMLElement ? document.activeElement : null;
  popup.hidden = false;
  popup.dataset.opened = 'true';
  popup.dataset.trigger = reason;
  document.body.classList.add('quote-popup-open');
  const card = popup.querySelector('.quote-popup-card');
  setTimeout(() => card?.focus(), 50);
  pushAnalyticsEvent('quote_popup_open', {source: reason, ...getTrackingContext()});
}

function closeQuotePopup(){
  const popup = document.querySelector('#quote-popup');
  if(!popup || popup.hidden) return;
  popup.hidden = true;
  document.body.classList.remove('quote-popup-open');
  try {
    window.localStorage?.setItem(QUOTE_POPUP_DISMISS_KEY, String(Date.now()));
    window.localStorage?.removeItem('terramorphQuotePopupDismissed');
  } catch(error) {
    console.warn('Popup storage write failed', error);
  }
  quotePopupReturnFocus?.focus?.();
  quotePopupReturnFocus = null;
}

function handleQuotePopupKeydown(event){
  const popup = document.querySelector('#quote-popup');
  if(!popup || popup.hidden) return;
  if(event.key === 'Escape'){
    event.preventDefault();
    closeQuotePopup();
    return;
  }
  if(event.key !== 'Tab') return;
  const focusable = getQuotePopupFocusableElements(popup);
  if(!focusable.length){
    event.preventDefault();
    popup.querySelector('.quote-popup-card')?.focus();
    return;
  }
  const first = focusable[0];
  const last = focusable[focusable.length - 1];
  if(event.shiftKey && document.activeElement === first){
    event.preventDefault();
    last.focus();
  } else if(!event.shiftKey && document.activeElement === last){
    event.preventDefault();
    first.focus();
  }
}

function scheduleQuotePopup(){
  const popup = document.querySelector('#quote-popup');
  if(!popup || document.body.classList.contains('quote-page') || document.querySelector('[data-funnel-service]')) return;
  let ready = false;
  const scrollDepth = () => {
    const scrollable = Math.max(document.documentElement.scrollHeight - window.innerHeight, 1);
    return window.scrollY / scrollable;
  };
  const openFromScroll = () => {
    if(ready && scrollDepth() >= 0.5) openQuotePopup('half_page_scroll');
  };
  const openFromExit = event => {
    if(ready && window.innerWidth >= 900 && event.clientY <= 0 && !event.relatedTarget){
      openQuotePopup('desktop_exit_intent');
    }
  };
  window.addEventListener('scroll', openFromScroll, {passive: true});
  document.addEventListener('mouseout', openFromExit);
  window.setTimeout(() => {
    ready = true;
    openFromScroll();
  }, QUOTE_POPUP_MIN_DELAY_MS);
  window.setTimeout(() => openQuotePopup('engaged_time'), QUOTE_POPUP_FALLBACK_MS);
}

const JOBBER_EMBED_SCRIPT = 'https://d3ey4dbjkt2f6s.cloudfront.net/assets/static_link/work_request_embed_snippet.js';

// The Jobber embed pulls ~1.4 MB (reCAPTCHA, Google Maps, Jobber's app) the
// moment its script runs. Load it only when the form is about to scroll into
// view, or immediately on tap. Attributes and IDs are exactly Jobber's own.
function loadJobberEmbed(holder){
  if(!holder || holder.dataset.jobberLoaded) return;
  holder.dataset.jobberLoaded = '1';
  holder.querySelector('[data-jobber-load]')?.remove();
  const script = document.createElement('script');
  script.src = JOBBER_EMBED_SCRIPT;
  script.setAttribute('clienthub_id', holder.dataset.clienthubId);
  script.setAttribute('form_url', holder.dataset.formUrl);
  holder.appendChild(script);
  pushAnalyticsEvent('jobber_form_loaded', {trigger: holder.dataset.jobberTrigger || 'scroll', ...getTrackingContext()});
}

function initLazyJobber(){
  const holders = [...document.querySelectorAll('[data-jobber-lazy]')];
  if(!holders.length) return;
  holders.forEach(holder => {
    holder.querySelector('[data-jobber-load]')?.addEventListener('click', () => {
      holder.dataset.jobberTrigger = 'tap';
      loadJobberEmbed(holder);
    });
  });
  // On the quote page the form IS the page: load it right away.
  if(document.body.classList.contains('quote-page') || !('IntersectionObserver' in window)){
    holders.forEach(loadJobberEmbed);
    return;
  }
  // Backup trigger in case the observer never reports (some in-app browsers).
  const nearCheck = () => {
    holders.forEach(holder => {
      if(!holder.dataset.jobberLoaded && holder.getBoundingClientRect().top < window.innerHeight + 900){
        loadJobberEmbed(holder);
      }
    });
    if(holders.every(holder => holder.dataset.jobberLoaded)) window.removeEventListener('scroll', nearCheck);
  };
  window.addEventListener('scroll', nearCheck, {passive: true});
  const io = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if(entry.isIntersecting){
        io.unobserve(entry.target);
        loadJobberEmbed(entry.target);
      }
    });
  }, {rootMargin: '900px 0px'});
  holders.forEach(holder => io.observe(holder));
}

// ---------- Phase 2 (v2 design) interactions. Each no-ops if its element is absent. ----------
function initTmChrome(){
  const header = document.querySelector('[data-tm-header]');
  const menuBtn = document.querySelector('[data-tm-menu]');
  const nav = document.getElementById('tm-nav');
  if(header){
    const solid = () => header.classList.toggle('is-solid', window.scrollY > 40);
    solid();
    window.addEventListener('scroll', solid, {passive: true});
  }
  if(menuBtn && nav){
    menuBtn.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      menuBtn.setAttribute('aria-expanded', String(open));
      if(open) header?.classList.add('is-solid');
    });
    nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
      nav.classList.remove('is-open');
      menuBtn.setAttribute('aria-expanded', 'false');
    }));
  }
  const bar = document.querySelector('[data-tm-bar]');
  const form = document.getElementById('request-form');
  if(bar && form && 'IntersectionObserver' in window){
    new IntersectionObserver(entries => {
      entries.forEach(entry => bar.classList.toggle('is-hidden', entry.isIntersecting));
    }, {threshold: 0.15}).observe(form);
  }
}

function initTmReveal(){
  if(document.body.classList.contains('tm-skin')){
    document.querySelectorAll('.section-heading, .why-grid > div, .authority-list > div, .local-specifics-grid > div, .guide-card, .ai-answer-card, .problem-card, .compact-review, .guide-content-block, .photo-carousel').forEach(el => el.classList.add('tm-reveal'));
  }
  const els = [...document.querySelectorAll('.tm-reveal')];
  if(!els.length) return;
  // Siblings come in one after another instead of all at once.
  els.forEach(el => {
    const sibs = el.parentElement ? [...el.parentElement.children].filter(c => c.classList.contains('tm-reveal')) : [el];
    const n = sibs.indexOf(el);
    if(n > 0) el.style.transitionDelay = (Math.min(n, 6) * 0.09).toFixed(2) + 's';
  });
  const showAll = () => els.forEach(el => el.classList.add('is-in'));
  if(!('IntersectionObserver' in window) || document.documentElement.classList.contains('tm-calm')){ showAll(); return; }
  document.documentElement.classList.add('tm-js');
  const io = new IntersectionObserver(entries => {
    entries.forEach(entry => { if(entry.isIntersecting){ entry.target.classList.add('is-in'); io.unobserve(entry.target); } });
  }, {rootMargin: '0px 0px -8% 0px'});
  els.forEach(el => io.observe(el));
  // Never leave content hidden if the observer is slow or unavailable.
  setTimeout(showAll, 2500);
}

function initTmBeforeAfter(){
  document.querySelectorAll('[data-ba]').forEach(box => {
    const range = box.querySelector('.tm-ba-range');
    if(!range) return;
    let used = false;
    const set = value => {
      box.style.setProperty('--pos', value + '%');
      if(!used){ used = true; pushAnalyticsEvent('slider_used', getTrackingContext()); }
    };
    range.addEventListener('input', () => set(range.value));
  });
}

function initTmMap(){
  const holder = document.querySelector('[data-leaflet]');
  const card = document.querySelector('[data-town-card]');
  if(!holder) return;
  let data;
  try { data = JSON.parse(holder.dataset.leaflet); } catch(e){ return; }
  let started = false;
  const start = () => {
    if(started) return;
    started = true;
    loadLeaflet().then(L => buildMap(L, holder, card, data)).catch(() => {
      holder.innerHTML = '<div class="tm-map-loading">Map unavailable. Pick your town from the list.</div>';
    });
  };
  const near = () => holder.getBoundingClientRect().top < window.innerHeight + 500;
  if('IntersectionObserver' in window){
    const io = new IntersectionObserver(entries => { if(entries.some(e => e.isIntersecting)){ io.disconnect(); start(); } }, {rootMargin: '500px 0px'});
    io.observe(holder);
  }
  // Backup for browsers or embedded views where the observer never fires.
  const onScroll = () => { if(near()){ window.removeEventListener('scroll', onScroll); start(); } };
  window.addEventListener('scroll', onScroll, {passive: true});
  onScroll();
}

function loadLeaflet(){
  if(window.L) return Promise.resolve(window.L);
  return new Promise((resolve, reject) => {
    const css = document.createElement('link');
    css.rel = 'stylesheet';
    css.href = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css';
    css.integrity = 'sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=';
    css.crossOrigin = '';
    document.head.appendChild(css);
    const js = document.createElement('script');
    js.src = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js';
    js.integrity = 'sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=';
    js.crossOrigin = '';
    js.onload = () => window.L ? resolve(window.L) : reject();
    js.onerror = reject;
    document.head.appendChild(js);
  });
}

function buildMap(L, holder, card, data){
  holder.innerHTML = '';
  const touch = window.matchMedia('(pointer: coarse)').matches;
  const map = L.map(holder, {zoomSnap: 0.25, zoomControl: false, scrollWheelZoom: false, dragging: !touch, tap: false, attributionControl: true});
  L.control.zoom({position: 'bottomright'}).addTo(map);
  map.attributionControl.setPrefix('<a href="https://leafletjs.com">Leaflet</a>');
  const minor = ['Ottawa Hills', 'Rossford', 'Monclova', 'Holland'];
  const zoomClass = () => holder.classList.toggle('tm-z-low', map.getZoom() < 11);
  map.on('zoomend', zoomClass);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 15, minZoom: 9,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map);
  const bounds = L.latLngBounds(data.towns.map(t => [t.la, t.lo]));
  map.fitBounds(bounds, {padding: touch ? [64, 26] : [60, 50]});
  zoomClass();
  const home = () => map.flyToBounds(bounds, {padding: touch ? [64, 26] : [60, 50], duration: 1});
  // Service zone grows out from the shop.
  const zone = L.circle([data.hq.la, data.hq.lo], {radius: 1, color: '#f1d384', weight: 1.5, fillColor: '#d8aa4d', fillOpacity: .09, className: 'tm-zone', interactive: false}).addTo(map);
  const target = 30000, t0 = performance.now();
  const grow = now => {
    const k = Math.min((now - t0) / 1600, 1);
    zone.setRadius(target * (1 - Math.pow(1 - k, 3)));
    if(k < 1) requestAnimationFrame(grow);
  };
  requestAnimationFrame(grow);
  L.marker([data.hq.la, data.hq.lo], {icon: L.divIcon({className: '', html: '<div class="tm-hq"><i></i><b>Terramorph HQ</b></div>', iconSize: [22, 22], iconAnchor: [11, 11]}), keyboard: false, interactive: false}).addTo(map);
  const left = ['Holland', 'Monclova', 'Waterville', 'Sylvania', 'Maumee', 'Toledo'].concat(touch ? [] : ['Whitehouse']);
  const pins = [];
  data.towns.forEach((t, i) => {
    const isLeft = left.includes(t.n);
    const icon = L.divIcon({className: '', html: '<div class="tm-pin' + (isLeft ? ' is-left' : '') + (minor.includes(t.n) ? ' is-minor' : '') + '" style="--d:' + (0.5 + i * 0.09).toFixed(2) + 's"><i></i><b>' + t.n + '</b></div>', iconSize: [14, 14], iconAnchor: isLeft ? [-0, 7] : [7, 7]});
    const m = L.marker([t.la, t.lo], {icon, title: t.n, alt: t.n, riseOnHover: true}).addTo(map);
    pins.push(m);
    m.on('click', () => {
      pins.forEach(p => p.getElement()?.querySelector('.tm-pin')?.classList.remove('is-on'));
      m.getElement()?.querySelector('.tm-pin')?.classList.add('is-on');
      map.flyTo([t.la, t.lo], 12, {duration: 1.1});
      if(card){
        const local = t.p !== 'service-areas.html';
        card.innerHTML = '<b>Yes, we serve ' + t.n + '.</b><p>Design, patios, drainage, lighting, maintenance, and cleanups in ' + t.n + ' and the surrounding area.</p>' +
          '<div class="tm-town-links">' + (local ? '<a class="tm-btn tm-btn-line tm-btn-sm" href="' + t.p + '">' + t.n + ' landscaping</a>' : '') +
          '<a class="tm-btn tm-btn-gold tm-btn-sm" href="#request-form">Get a free quote</a><button type="button" class="tm-btn tm-btn-line tm-btn-sm" data-map-reset>Show all towns</button></div>';
        card.querySelector('[data-map-reset]')?.addEventListener('click', () => { pins.forEach(p => p.getElement()?.querySelector('.tm-pin')?.classList.remove('is-on')); home(); });
        card.classList.remove('tm-card-pop'); void card.offsetWidth; card.classList.add('tm-card-pop');
      }
      pushAnalyticsEvent('map_town_tapped', {town: t.n, ...getTrackingContext()});
    });
  });
}

if(/[?&]calm\b/.test(window.location.search)) document.documentElement.classList.add('tm-calm');

// Site-wide motion: scroll progress, hero drift, headline word rise, count-ups,
// card tilt and the How-it-works timeline. Everything is skipped for visitors
// who ask for reduced motion.
function initTmMotion(){
  const calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches || document.documentElement.classList.contains('tm-calm');
  // Timeline + any [data-inview] block: add .is-in once on screen.
  const inview = [...document.querySelectorAll('[data-proc], [data-inview]')];
  if(calm || !('IntersectionObserver' in window)){ inview.forEach(el => el.classList.add('is-in')); }
  else {
    const io = new IntersectionObserver(entries => entries.forEach(e => { if(e.isIntersecting){ e.target.classList.add('is-in'); io.unobserve(e.target); } }), {rootMargin: '0px 0px -18% 0px'});
    inview.forEach(el => io.observe(el));
    // Backup: never leave a block un-played if the observer stays silent.
    const check = () => {
      inview.forEach(el => { const r = el.getBoundingClientRect(); if(r.top < window.innerHeight * 0.85 && r.bottom > 0) el.classList.add('is-in'); });
      if(inview.every(el => el.classList.contains('is-in'))) window.removeEventListener('scroll', check);
    };
    window.addEventListener('scroll', check, {passive: true});
    check();
  }
  if(calm) return;
  // Thin gold scroll-progress line.
  const bar = document.createElement('div');
  bar.className = 'tm-progress';
  bar.setAttribute('aria-hidden', 'true');
  document.body.appendChild(bar);
  // Hero photo drifts slower than the page.
  const media = document.querySelector('.tm-hero-media, .page-hero-image');
  let ticking = false;
  const onScroll = () => {
    if(ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      const y = window.scrollY;
      const max = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(y / max, 1) : 0) + ')';
      if(media && y < window.innerHeight * 1.2) media.style.transform = 'translate3d(0,' + (y * 0.22).toFixed(1) + 'px,0)';
      ticking = false;
    });
  };
  window.addEventListener('scroll', onScroll, {passive: true});
  onScroll();
  // Inner-page headlines rise in word by word.
  const h1 = document.querySelector('.page-hero h1');
  if(h1 && !h1.querySelector('.tm-w')){
    const words = h1.textContent.trim().split(/\s+/);
    h1.setAttribute('aria-label', h1.textContent.trim());
    h1.innerHTML = words.map((w, i) => '<span class="tm-w" aria-hidden="true" style="animation-delay:' + (0.05 + i * 0.055).toFixed(2) + 's">' + w.replace(/[&<>]/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;'})[c]) + '</span>').join(' ');
    h1.classList.add('tm-split');
  }
  // Numbers count up when they come into view (220+, 4.9).
  const counters = [...document.querySelectorAll('.trust-feature strong, .tm-rating-big b')].filter(el => /^\d+(\.\d)?\+?$/.test(el.textContent.trim()));
  if(counters.length && 'IntersectionObserver' in window){
    const cio = new IntersectionObserver(entries => entries.forEach(e => {
      if(!e.isIntersecting) return;
      cio.unobserve(e.target);
      const el = e.target, raw = el.textContent.trim(), plus = raw.endsWith('+') ? '+' : '';
      const end = parseFloat(raw), dec = raw.includes('.') ? 1 : 0, t0 = performance.now();
      const tick = now => {
        const k = Math.min((now - t0) / 1400, 1), v = end * (1 - Math.pow(1 - k, 3));
        el.textContent = v.toFixed(dec) + (k === 1 ? plus : '');
        if(k < 1) requestAnimationFrame(tick); else el.textContent = raw;
      };
      requestAnimationFrame(tick);
    }), {threshold: 0.6});
    counters.forEach(el => cio.observe(el));
  }
  // Subtle 3D tilt on photo tiles and guide cards (mouse only).
  if(window.matchMedia('(hover: hover) and (pointer: fine)').matches){
    document.querySelectorAll('.tm-tile, .guide-card').forEach(card => {
      card.addEventListener('pointermove', e => {
        const r = card.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
        card.style.transform = 'perspective(900px) rotateY(' + (x * 5).toFixed(2) + 'deg) rotateX(' + (-y * 5).toFixed(2) + 'deg) translateY(-4px)';
      });
      card.addEventListener('pointerleave', () => { card.style.transform = ''; });
    });
  }
}

// Homepage "What is going on with your yard?" picker.
function initTmPicker(){
  const box = document.querySelector('[data-picker]');
  if(!box) return;
  const opts = [...box.querySelectorAll('[data-pick]')];
  const panes = [...box.querySelectorAll('[data-pane]')];
  opts.forEach(btn => btn.addEventListener('click', () => {
    const key = btn.dataset.pick;
    opts.forEach(o => o.setAttribute('aria-pressed', String(o === btn)));
    panes.forEach(p => {
      const on = p.dataset.pane === key;
      p.hidden = !on;
      p.classList.toggle('is-on', on);
      p.classList.remove('is-entering');
      if(on){ void p.offsetWidth; p.classList.add('is-entering'); }
    });
    if(window.matchMedia('(max-width: 900px)').matches){
      btn.scrollIntoView({behavior: 'smooth', block: 'nearest', inline: 'center'});
    }
    pushAnalyticsEvent('yard_picker_choice', {choice: key, ...getTrackingContext()});
  }));
  box.querySelectorAll('[data-pick-cta]').forEach(a => a.addEventListener('click', () => {
    pushAnalyticsEvent('yard_picker_quote_click', {choice: a.dataset.pickCta, ...getTrackingContext()});
  }));
}

// Before/after cards: wipe from the before shot to the after shot when they
// scroll into view; the Before/After pills switch back and forth.
function initTmFlip(){
  const cards = [...document.querySelectorAll('[data-flip]')];
  if(!cards.length) return;
  const show = (card, which) => {
    card.classList.toggle('show-after', which === 'after');
    card.querySelectorAll('[data-show]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.show === which)));
  };
  cards.forEach(card => {
    show(card, 'before');
    card.querySelectorAll('[data-show]').forEach(b => b.addEventListener('click', e => { e.stopPropagation(); card.dataset.played = '1'; show(card, b.dataset.show); }));
    card.querySelector('.tm-flip-media')?.addEventListener('click', () => { card.dataset.played = '1'; show(card, card.classList.contains('show-after') ? 'before' : 'after'); });
  });
  const play = card => { if(card.dataset.played) return; card.dataset.played = '1'; setTimeout(() => show(card, 'after'), 900); };
  const check = () => cards.forEach(card => { const r = card.getBoundingClientRect(); if(r.top < window.innerHeight * 0.75 && r.bottom > 0) play(card); });
  window.addEventListener('scroll', check, {passive: true});
  if('IntersectionObserver' in window){
    const io = new IntersectionObserver(es => es.forEach(e => { if(e.isIntersecting){ play(e.target); io.unobserve(e.target); } }), {threshold: 0.45});
    cards.forEach(c => io.observe(c));
  }
  check();
}

// Gallery photos carry data-src until the gallery is close to the screen,
// so they never compete with the page's first photo for bandwidth.
function hydrateCarousel(carousel){
  carousel.querySelectorAll('img[data-src]').forEach(img => {
    if(img.dataset.srcset) img.srcset = img.dataset.srcset;
    img.src = img.dataset.src;
    img.removeAttribute('data-src');
    img.removeAttribute('data-srcset');
  });
}

function watchCarouselLoad(carousel, then){
  if(!carousel.querySelector('img[data-src]') && !then) return;
  let done = false;
  const near = () => { const r = carousel.getBoundingClientRect(); return r.top < window.innerHeight + 600 && r.bottom > -600; };
  const go = () => { if(done) return; done = true; window.removeEventListener('scroll', onScroll); hydrateCarousel(carousel); if(then) then(); };
  const onScroll = () => { if(near()) go(); };
  if('IntersectionObserver' in window){
    const io = new IntersectionObserver(es => { if(es.some(e => e.isIntersecting)){ io.disconnect(); go(); } }, {rootMargin: '600px 0px'});
    io.observe(carousel);
  }
  window.addEventListener('scroll', onScroll, {passive: true});
  requestAnimationFrame(() => setTimeout(onScroll, 0));
}

function initCarousels(){
  const calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches || document.documentElement.classList.contains('tm-calm');
  document.querySelectorAll('[data-carousel]').forEach(carousel => {
    const track = carousel.querySelector('.carousel-track');
    if(!track) return;
    const step = () => Math.max(track.clientWidth * 0.8, 240);
    if(carousel.classList.contains('photo-carousel') && !calm){
      // Set up the glide only when the gallery is about to be seen, so page load stays light.
      watchCarouselLoad(carousel, () => initGlide(carousel, track, step));
      return;
    }
    watchCarouselLoad(carousel);
    const go = dir => track.scrollBy({left: dir * step(), behavior: 'smooth'});
    carousel.querySelector('[data-carousel-prev]')?.addEventListener('click', () => go(-1));
    carousel.querySelector('[data-carousel-next]')?.addEventListener('click', () => go(1));
    let timer = null;
    const stop = () => { if(timer){ clearInterval(timer); timer = null; } };
    const start = () => {
      if(timer) return;
      timer = setInterval(() => {
        if(track.scrollLeft + track.clientWidth >= track.scrollWidth - 8){
          track.scrollTo({left: 0, behavior: 'smooth'});
        } else {
          go(1);
        }
      }, 4500);
    };
    ['pointerenter', 'pointerdown', 'focusin', 'touchstart'].forEach(ev => carousel.addEventListener(ev, stop, {passive: true}));
    carousel.addEventListener('pointerleave', start);
    if(!calm) start();
  });
}

// Project photos glide continuously in a seamless loop; touching, hovering or
// using the arrows pauses the glide, and it picks back up a few seconds later.
function initGlide(carousel, track, step){
  const originals = [...track.children];
  originals.forEach(slide => {
    const copy = slide.cloneNode(true);
    copy.setAttribute('aria-hidden', 'true');
    copy.querySelectorAll('img').forEach(img => { img.alt = ''; });
    track.appendChild(copy);
  });
  carousel.classList.add('is-gliding');
  track.style.scrollSnapType = 'none';
  track.style.scrollBehavior = 'auto';
  const SPEED = 38; // px per second
  let pos = 0, last = 0, visible = false, pausedUntil = 0, hovering = false;
  const half = () => track.scrollWidth / 2;
  const pause = ms => { pausedUntil = performance.now() + ms; };
  const frame = now => {
    const dt = last ? Math.min(now - last, 64) : 16;
    last = now;
    if(visible && !hovering && now > pausedUntil && half() > track.clientWidth){
      if(Math.abs(track.scrollLeft - pos) > 2) pos = track.scrollLeft; // user moved it
      pos += SPEED * dt / 1000;
      if(pos >= half()) pos -= half();
      track.scrollLeft = pos;
    }
    requestAnimationFrame(frame);
  };
  const jump = dir => {
    pause(5000);
    let target = track.scrollLeft + dir * step();
    if(target < 0) { track.scrollLeft += half(); target += half(); }
    track.scrollTo({left: target, behavior: 'smooth'});
  };
  carousel.querySelector('[data-carousel-prev]')?.addEventListener('click', () => jump(-1));
  carousel.querySelector('[data-carousel-next]')?.addEventListener('click', () => jump(1));
  carousel.addEventListener('pointerenter', e => { if(e.pointerType === 'mouse') hovering = true; });
  carousel.addEventListener('pointerleave', () => { hovering = false; pos = track.scrollLeft; });
  ['pointerdown', 'touchstart', 'wheel', 'focusin'].forEach(ev => carousel.addEventListener(ev, () => pause(3500), {passive: true}));
  track.addEventListener('scroll', () => { if(track.scrollLeft >= half()) { track.scrollLeft -= half(); pos = track.scrollLeft; } }, {passive: true});
  if('IntersectionObserver' in window){
    new IntersectionObserver(entries => { visible = entries[0].isIntersecting; }, {rootMargin: '100px'}).observe(carousel);
  } else {
    visible = true;
  }
  requestAnimationFrame(frame);
}

document.addEventListener('DOMContentLoaded', () => {
  initCarousels();
  initTmChrome();
  initTmReveal();
  initTmBeforeAfter();
  initTmMap();
  initTmMotion();
  initTmPicker();
  initTmFlip();
  persistTrackingContext();
  // Must run BEFORE decorateAttributionLinks() so the hosted-form button it
  // creates gets the utm/fbclid query string appended, and before the
  // clienthub click handlers below bind to it.
  routePaidTrafficToHostedForm();
  decorateAttributionLinks();
  pushAnalyticsEvent('terramorph_page_view', getTrackingContext());
  if(document.querySelector('[data-funnel-service]')){
    metaTrack('ViewContent', {content_name: 'Terramorph service landing page', content_category: getTrackingContext().service_category, ...getTrackingContext()});
  } else if(document.body.classList.contains('tm-svc')){
    // Main service pages: lets Meta build audiences of people who looked at a service.
    metaTrack('ViewContent', {content_name: document.title, content_category: 'service_page', ...getTrackingContext()});
  }
  trackAttributedThankYouView();
  watchJobberFormSubmission();
  initLazyJobber();
  document.querySelectorAll('.links a').forEach(link => link.addEventListener('click', () => {
    const menu = document.querySelector('.links');
    const button = document.querySelector('.mobile-menu');
    menu?.classList.remove('open');
    button?.setAttribute('aria-expanded', 'false');
  }));
  document.querySelectorAll('a[href^="tel:"]').forEach(link => {
    link.addEventListener('click', () => trackPhoneClick(link));
  });
  document.querySelectorAll('[data-quote-service]').forEach(link => {
    link.addEventListener('click', () => trackQuoteIntent('phone_quote', link));
  });
  document.querySelectorAll('a[href*="quote.html"], a[href="#request-form"], a[href="#quote"]').forEach(link => {
    if(link.matches('[data-quote-service]')) return;
    link.addEventListener('click', () => trackQuoteIntent('website_quote_link', link));
  });
  document.querySelectorAll('a[href*="clienthub.getjobber.com"]').forEach(link => {
    link.addEventListener('click', () => trackQuoteIntent('jobber_direct', link));
  });
  document.querySelectorAll('[data-quick-lead-form]').forEach(form => {
    form.addEventListener('submit', event => handleQuickLeadSubmit(form, event));
  });
  document.querySelectorAll('[data-request-form]').forEach(form => {
    form.addEventListener('submit', event => handleRequestFormSubmit(form, event));
  });
  document.querySelectorAll('[data-close-popup]').forEach(el => el.addEventListener('click', closeQuotePopup));
  document.addEventListener('keydown', handleQuotePopupKeydown);
  scheduleQuotePopup();
});
