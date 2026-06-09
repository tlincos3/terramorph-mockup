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
    link.href = JOBBER_SOURCE_URLS[source];
    link.dataset.jobberSource = source;
  });
}

function trackQuoteIntent(source){
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({event:'quote_intent', source: source || 'jobber', jobber_source: getJobberSource() || 'direct'});
  if(typeof fbq === 'function') fbq('track', 'Lead');
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
  document.querySelectorAll('.links a').forEach(link => link.addEventListener('click', () => {
    const menu = document.querySelector('.links');
    const button = document.querySelector('.mobile-menu');
    menu?.classList.remove('open');
    button?.setAttribute('aria-expanded', 'false');
  }));
  document.querySelectorAll('a[href*="clienthub.getjobber.com"], a[href="#quote"]').forEach(link => {
    link.addEventListener('click', () => trackQuoteIntent(link.href.includes('clienthub') ? 'jobber_direct' : 'onsite_quote'));
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
