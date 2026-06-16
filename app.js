function toggleMenu(button){
  const menu = document.querySelector('.links');
  if(!menu) return;
  const open = menu.classList.toggle('open');
  if(button) button.setAttribute('aria-expanded', String(open));
}

const JOBBER_SOURCE_URLS = {
  facebook: 'https://clienthub.getjobber.com/hubs/e644a784-b214-4a2b-93df-ace28dbb2a70/public/requests/1578803/new?utm_source=facebook&source=social_media',
  google: 'https://clienthub.getjobber.com/hubs/e644a784-b214-4a2b-93df-ace28dbb2a70/public/requests/1578803/new?utm_source=google&source=social_media',
  instagram: 'https://clienthub.getjobber.com/hubs/e644a784-b214-4a2b-93df-ace28dbb2a70/public/requests/1578803/new?utm_source=instagram&source=social_media'
};

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

function applyJobberAttribution(){
  const source = getJobberSource();
  if(!source) return;
  document.querySelectorAll('a[href*="clienthub.getjobber.com/hubs/e644a784-b214-4a2b-93df-ace28dbb2a70/public/requests/1578803/new"]').forEach(link => {
    const url = new URL(link.href);
    url.searchParams.set('utm_source', source);
    url.searchParams.set('source', 'social_media');
    if(!url.searchParams.get('utm_medium')) url.searchParams.set('utm_medium', 'website');
    link.href = url.toString();
    link.dataset.jobberSource = source;
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

function getTrackingContext(){
  const service = document.querySelector('[data-funnel-service]')?.dataset.funnelService || document.querySelector('[data-service]')?.dataset.service || '';
  return {
    page_title: document.title,
    page_path: window.location.pathname,
    page_url: window.location.href,
    service_category: service || 'general',
    jobber_source: getJobberSource() || 'direct'
  };
}

function trackQuoteIntent(source){
  const context = {source: source || 'jobber', ...getTrackingContext()};
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({event:'quote_intent', ...context});
  metaTrack('Lead', {content_name: 'Terramorph quote intent', content_category: context.source, ...context});
}

function trackPhoneClick(link){
  const context = {source: 'phone_click', phone_number: (link?.getAttribute('href') || '').replace(/^tel:/, ''), ...getTrackingContext()};
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({event:'phone_click', ...context});
  metaTrack('Lead', {content_name: 'Terramorph phone lead', content_category: 'phone_call', lead_type: 'phone_call', ...context});
  metaTrack('Contact', {content_name: 'Terramorph phone click', content_category: 'phone_call', ...context});
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
  applyJobberAttribution();
  if(document.querySelector('[data-funnel-service]')){
    metaTrack('ViewContent', {content_name: 'Terramorph service landing page', content_category: getTrackingContext().service_category, ...getTrackingContext()});
  }
  if(window.location.pathname.endsWith('/thank-you.html') || window.location.pathname.endsWith('/thank-you')){
    trackQuoteIntent('thank_you_page');
  }
  document.querySelectorAll('.links a').forEach(link => link.addEventListener('click', () => {
    const menu = document.querySelector('.links');
    const button = document.querySelector('.mobile-menu');
    menu?.classList.remove('open');
    button?.setAttribute('aria-expanded', 'false');
  }));
  document.querySelectorAll('a[href*="clienthub.getjobber.com"], a[href="#quote"]').forEach(link => {
    link.addEventListener('click', () => trackQuoteIntent(link.href.includes('clienthub') ? 'jobber_direct' : 'onsite_quote'));
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
