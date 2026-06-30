function toggleMenu(button){
  const menu = document.querySelector('.links');
  if(!menu) return;
  const open = menu.classList.toggle('open');
  if(button) button.setAttribute('aria-expanded', String(open));
}

const TERRAMORPH_PHONE_HREF = 'tel:4198736801';
const TERRAMORPH_PHONE_DISPLAY = '419-873-6801';
const JOBBER_REQUEST_PATH = 'terramorph-disabled-jobber-request-path';
const JOBBER_SOURCE_URLS = {};
const TRACKING_STORAGE_KEY = 'terramorphAttributionContext';
const PENDING_JOBBER_KEY = 'terramorphPendingJobberLead';
const QUICK_LEAD_KEY = 'terramorphQuickLeadContext';
const SOCIAL_SOURCES = new Set(['facebook', 'instagram', 'google']);
const TRACKING_PARAM_KEYS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'fbclid', 'gclid', 'msclkid'];
const THANK_YOU_LEAD_KEY = 'terramorphThankYouLeadTracked';


function initLazyJobberForms(){
  // Quote and request actions are phone-first now.
}

function getJobberSource(){
  const params = new URLSearchParams(window.location.search);
  const directSource = (params.get('utm_source') || params.get('source') || '').toLowerCase();
  if(JOBBER_SOURCE_URLS[directSource]) return directSource;
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
    const detectedSource = getJobberSource();
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

function applyJobberContextToUrl(inputUrl){
  const url = new URL(inputUrl, window.location.origin);
  const context = getMergedTrackingContext();
  TRACKING_PARAM_KEYS.forEach(key => {
    if(context[key]) url.searchParams.set(key, context[key]);
  });
  if(!url.searchParams.get('utm_source') && context.utm_source) url.searchParams.set('utm_source', context.utm_source);
  if(!url.searchParams.get('utm_medium')){
    url.searchParams.set('utm_medium', context.utm_medium || 'website');
  }
  if(context.utm_source && SOCIAL_SOURCES.has(String(context.utm_source).toLowerCase()) && !url.searchParams.get('source')){
    url.searchParams.set('source', 'social_media');
  }
  return url;
}

function applyJobberAttribution(){
  document.querySelectorAll(`a[href*="${JOBBER_REQUEST_PATH}"]`).forEach(link => {
    const url = applyJobberContextToUrl(link.href);
    link.href = url.toString();
    link.dataset.jobberSource = url.searchParams.get('utm_source') || getJobberSource() || 'direct';
  });
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
    jobber_source: stored.utm_source || getJobberSource() || 'direct',
    utm_source: stored.utm_source || '',
    utm_medium: stored.utm_medium || '',
    utm_campaign: stored.utm_campaign || '',
    utm_content: stored.utm_content || '',
    utm_term: stored.utm_term || '',
    fbclid: stored.fbclid || '',
    gclid: stored.gclid || '',
    msclkid: stored.msclkid || '',
    fbp: stored.fbp || getCookieValue('_fbp') || '',
    fbc: stored.fbc || getCookieValue('_fbc') || getFbcFromFbclid(stored.fbclid) || '',
    lead_service: quickLead.service || '',
    lead_city: quickLead.city || '',
    lead_timeline: quickLead.timeline || ''
  };
}

function trackQuoteIntent(source, link){
  const context = {
    source: source || 'jobber',
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
  metaTrack('Lead', {content_name: 'Terramorph phone lead', content_category: 'phone_call', lead_type: 'phone_call', ...context});
  metaTrack('Contact', {content_name: 'Terramorph phone click', content_category: 'phone_call', ...context});
}

function storePendingJobberLead(link){
  if(!link?.href || !link.href.includes(JOBBER_REQUEST_PATH)) return;
  const jobberUrl = applyJobberContextToUrl(link.href);
  const id = `${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;
  writeStoredJson(PENDING_JOBBER_KEY, {
    id,
    created_at: new Date().toISOString(),
    destination_url: jobberUrl.toString(),
    ...getMergedTrackingContext()
  });
}

function trackCompletedQuoteLead(){
  const pending = readStoredJson(PENDING_JOBBER_KEY);
  if(!pending?.id) return;
  const createdAtMs = Date.parse(pending.created_at || '');
  if(!Number.isFinite(createdAtMs) || (Date.now() - createdAtMs) > (1000 * 60 * 60 * 6)){
    window.localStorage?.removeItem(PENDING_JOBBER_KEY);
    return;
  }
  const context = {
    source: 'jobber_thank_you',
    ...getTrackingContext(),
    utm_source: pending.utm_source || '',
    utm_medium: pending.utm_medium || '',
    utm_campaign: pending.utm_campaign || '',
    utm_content: pending.utm_content || '',
    fbclid: pending.fbclid || '',
    jobber_destination: pending.destination_url || ''
  };
  pushAnalyticsEvent('quote_submit', context);
  metaTrack('Lead', {content_name: 'Terramorph quote request submitted', content_category: 'jobber_submission', lead_stage: 'submitted', ...context}, {eventId: `jobber-submission-${pending.id}`});
  metaTrackCustom('QuoteSubmitted', context);
  window.localStorage?.removeItem(PENDING_JOBBER_KEY);
  window.sessionStorage?.setItem(THANK_YOU_LEAD_KEY, pending.id);
}

function trackThankYouFallbackLead(){
  if(!(window.location.pathname.endsWith('/thank-you.html') || window.location.pathname.endsWith('/thank-you'))) return;
  if(window.sessionStorage?.getItem(THANK_YOU_LEAD_KEY)) return;
  const context = getTrackingContext();
  const hasAttributionContext = Boolean(
    context.fbclid || context.gclid || context.msclkid ||
    context.utm_source || context.utm_campaign ||
    context.lead_service || context.lead_city || context.lead_timeline
  );
  if(!hasAttributionContext){
    pushAnalyticsEvent('quote_thank_you_view_unattributed', {source: 'thank_you_page_unattributed', ...context});
    return;
  }
  const eventId = `thank-you-${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;
  const fallbackContext = {
    source: 'thank_you_page_attributed_fallback',
    lead_stage: 'submitted_or_returned',
    ...context
  };
  pushAnalyticsEvent('quote_submit_fallback', fallbackContext);
  metaTrackCustom('QuoteThankYouFallback', fallbackContext);
  window.sessionStorage?.setItem(THANK_YOU_LEAD_KEY, eventId);
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

function getQuickLeadJobberUrl(form, quickLead){
  const base = form.dataset.jobberUrl || JOBBER_SOURCE_URLS.facebook || `https://${JOBBER_REQUEST_PATH}`;
  const url = applyJobberContextToUrl(base);
  const params = {
    tm_lead_source: 'quick_form',
    tm_name: quickLead.name,
    tm_phone: quickLead.phone,
    tm_city: quickLead.city,
    tm_service: quickLead.service,
    tm_timeline: quickLead.timeline,
    tm_problem: quickLead.problem
  };
  Object.entries(params).forEach(([key, value]) => {
    if(value) url.searchParams.set(key, value);
  });
  return url;
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
  writeStoredJson(QUICK_LEAD_KEY, {
    ...quickLead,
    event_id: eventId,
    created_at: new Date().toISOString(),
    ...getMergedTrackingContext()
  });
  writeStoredJson(PENDING_JOBBER_KEY, {
    id: eventId,
    created_at: new Date().toISOString(),
    destination_url: TERRAMORPH_PHONE_HREF,
    quick_lead: true,
    phone_call: true,
    ...getMergedTrackingContext()
  });
  pushAnalyticsEvent('quick_lead_continue', context);
  metaTrack('Lead', {content_name: 'Terramorph quick quote lead', content_category: quickLead.service || 'paid_landing', ...context}, {eventId});
  metaTrackCustom('QuickLeadContinue', context);
  if(button){
    button.disabled = true;
    button.textContent = `Calling ${TERRAMORPH_PHONE_DISPLAY}...`;
  }
  if(status) status.textContent = `Good - opening your phone so you can call Terramorph at ${TERRAMORPH_PHONE_DISPLAY}.`;
  window.location.href = TERRAMORPH_PHONE_HREF;
}

function openQuotePopup(){
  const popup = document.querySelector('#quote-popup');
  if(!popup || popup.dataset.opened === 'true') return;
  if(window.localStorage?.getItem('terramorphQuotePopupDismissed') === '1') return;
  popup.hidden = false;
  popup.dataset.opened = 'true';
  document.body.classList.add('quote-popup-open');
  const card = popup.querySelector('.quote-popup-card');
  setTimeout(() => card?.focus(), 50);
}

function closeQuotePopup(){
  const popup = document.querySelector('#quote-popup');
  if(!popup) return;
  popup.hidden = true;
  document.body.classList.remove('quote-popup-open');
  window.localStorage?.setItem('terramorphQuotePopupDismissed', '1');
}

document.addEventListener('DOMContentLoaded', () => {
  persistTrackingContext();
  pushAnalyticsEvent('terramorph_page_view', getTrackingContext());
  applyJobberAttribution();
  initLazyJobberForms();
  if(document.querySelector('[data-funnel-service]')){
    metaTrack('ViewContent', {content_name: 'Terramorph service landing page', content_category: getTrackingContext().service_category, ...getTrackingContext()});
  }
  if(window.location.pathname.endsWith('/thank-you.html') || window.location.pathname.endsWith('/thank-you')){
    trackCompletedQuoteLead();
    trackThankYouFallbackLead();
  }
  document.querySelectorAll('.links a').forEach(link => link.addEventListener('click', () => {
    const menu = document.querySelector('.links');
    const button = document.querySelector('.mobile-menu');
    menu?.classList.remove('open');
    button?.setAttribute('aria-expanded', 'false');
  }));
  document.querySelectorAll(`a[href*="${JOBBER_REQUEST_PATH}"], a[href="#quote"]`).forEach(link => {
    link.addEventListener('click', () => {
      if(link.href.includes(JOBBER_REQUEST_PATH)){
        storePendingJobberLead(link);
        trackQuoteIntent('jobber_direct', link);
      } else {
        trackQuoteIntent('onsite_quote', link);
      }
    });
  });
  document.querySelectorAll('a[href^="tel:"]').forEach(link => {
    link.addEventListener('click', () => trackPhoneClick(link));
  });
  document.querySelectorAll('[data-quick-lead-form]').forEach(form => {
    form.addEventListener('submit', event => handleQuickLeadSubmit(form, event));
  });
  document.querySelectorAll('[data-close-popup]').forEach(el => el.addEventListener('click', closeQuotePopup));
  document.addEventListener('keydown', event => { if(event.key === 'Escape') closeQuotePopup(); });

  const labelJobberIframes = () => {
    document.querySelectorAll('.jobber-embed-wrap iframe').forEach(frame => {
      if(!frame.getAttribute('title')){
        frame.setAttribute('title', 'Terramorph secure quote request form');
      }
    });
  };

  labelJobberIframes();
  window.setTimeout(labelJobberIframes, 750);
  window.setTimeout(labelJobberIframes, 2500);
  if('MutationObserver' in window){
    const jobberObserver = new MutationObserver(labelJobberIframes);
    document.querySelectorAll('.jobber-embed-wrap').forEach(wrap => {
      jobberObserver.observe(wrap, { childList: true, subtree: true });
    });
  }

  window.setTimeout(() => {
    document.querySelectorAll('.jobber-quote-panel').forEach(panel => {
      const wrap = panel.querySelector('.jobber-embed-wrap');
      if(wrap && /Form is currently unavailable|Something went wrong/i.test(wrap.textContent || '')){
        panel.classList.add('jobber-embed-unavailable');
      }
    });
  }, 2500);

  window.setTimeout(openQuotePopup, 12000);
});
