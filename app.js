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

function trackPhoneClick(link){
  const context = {source: 'phone_click', phone_number: (link?.getAttribute('href') || '').replace(/^tel:/, ''), ...getTrackingContext()};
  pushAnalyticsEvent('phone_click', context);
  metaTrack('Contact', {content_name: 'Terramorph phone click', content_category: 'phone_call', ...context});
  metaTrackCustom('PhoneClick', context);
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
  const normalizedSource = String(context.utm_source || '').trim().toLowerCase();
  const hasMetaAttributionContext = normalizedSource
    ? META_SOURCES.has(normalizedSource)
    : Boolean(context.fbclid || context.fbc || context.fb_campaign_id || context.fb_adset_id || context.fb_ad_id);
  // Meta Lead is reserved for Meta-attributed submissions. Sending every paid
  // or organic Jobber completion to Meta would contaminate optimization data.
  if(hasMetaAttributionContext){
    metaTrack('Lead', {content_name: 'Terramorph quote request', content_category: context.service_category || 'quote_request', ...attributionContext}, {eventId});
    metaTrackCustom('QuoteThankYouAttribution', attributionContext);
  }
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
  const normalizedSource = String(context.utm_source || '').trim().toLowerCase();
  const hasMetaAttributionContext = normalizedSource
    ? META_SOURCES.has(normalizedSource)
    : Boolean(context.fbclid || context.fbc || context.fb_campaign_id || context.fb_adset_id || context.fb_ad_id);
  if(hasMetaAttributionContext){
    metaTrack('Lead', {content_name: 'Terramorph quote request', content_category: context.service_category || 'quote_request', ...context}, {eventId});
    metaTrackCustom('JobberRequestSubmitted', context);
  }
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

function initCarousels(){
  document.querySelectorAll('[data-carousel]').forEach(carousel => {
    const track = carousel.querySelector('.carousel-track');
    if(!track) return;
    const step = () => Math.max(track.clientWidth * 0.8, 240);
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
    if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches) start();
  });
}

document.addEventListener('DOMContentLoaded', () => {
  initCarousels();
  persistTrackingContext();
  decorateAttributionLinks();
  pushAnalyticsEvent('terramorph_page_view', getTrackingContext());
  if(document.querySelector('[data-funnel-service]')){
    metaTrack('ViewContent', {content_name: 'Terramorph service landing page', content_category: getTrackingContext().service_category, ...getTrackingContext()});
  }
  trackAttributedThankYouView();
  watchJobberFormSubmission();
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
