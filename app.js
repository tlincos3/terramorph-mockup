function toggleMenu(button){
  const menu = document.querySelector('.links');
  if(!menu) return;
  const open = menu.classList.toggle('open');
  if(button) button.setAttribute('aria-expanded', String(open));
}

const JOBBER_REQUEST_PATH = 'clienthub.getjobber.com/hubs/e644a784-b214-4a2b-93df-ace28dbb2a70/public/requests/1578803/new';
const JOBBER_SOURCE_URLS = {
  facebook: 'https://clienthub.getjobber.com/hubs/e644a784-b214-4a2b-93df-ace28dbb2a70/public/requests/1578803/new?utm_source=facebook&source=social_media',
  google: 'https://clienthub.getjobber.com/hubs/e644a784-b214-4a2b-93df-ace28dbb2a70/public/requests/1578803/new?utm_source=google&source=social_media',
  instagram: 'https://clienthub.getjobber.com/hubs/e644a784-b214-4a2b-93df-ace28dbb2a70/public/requests/1578803/new?utm_source=instagram&source=social_media'
};
const TRACKING_STORAGE_KEY = 'terramorphAttributionContext';
const PENDING_JOBBER_KEY = 'terramorphPendingJobberLead';
const SOCIAL_SOURCES = new Set(['facebook', 'instagram', 'google']);
const TRACKING_PARAM_KEYS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'fbclid', 'gclid', 'msclkid'];

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

function getTrackingContext(){
  const stored = getMergedTrackingContext();
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
    fbclid: stored.fbclid || ''
  };
}

function trackQuoteIntent(source, link){
  const context = {
    source: source || 'jobber',
    destination_url: link?.href || '',
    ...getTrackingContext()
  };
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({event:'quote_intent', ...context});
  metaTrack('Contact', {content_name: 'Terramorph quote intent', content_category: context.source, lead_stage: 'intent', ...context});
  metaTrackCustom('QuoteIntent', context);
}

function trackPhoneClick(link){
  const context = {source: 'phone_click', phone_number: (link?.getAttribute('href') || '').replace(/^tel:/, ''), ...getTrackingContext()};
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({event:'phone_click', ...context});
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
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({event:'quote_submit', ...context});
  metaTrack('Lead', {content_name: 'Terramorph quote request submitted', content_category: 'jobber_submission', lead_stage: 'submitted', ...context}, {eventId: `jobber-submission-${pending.id}`});
  metaTrackCustom('QuoteSubmitted', context);
  window.localStorage?.removeItem(PENDING_JOBBER_KEY);
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
  applyJobberAttribution();
  if(document.querySelector('[data-funnel-service]')){
    metaTrack('ViewContent', {content_name: 'Terramorph service landing page', content_category: getTrackingContext().service_category, ...getTrackingContext()});
  }
  if(window.location.pathname.endsWith('/thank-you.html') || window.location.pathname.endsWith('/thank-you')){
    trackCompletedQuoteLead();
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
  document.querySelectorAll('[data-close-popup]').forEach(el => el.addEventListener('click', closeQuotePopup));
  document.addEventListener('keydown', event => { if(event.key === 'Escape') closeQuotePopup(); });

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
