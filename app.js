function toggleMenu(button){
  const menu = document.querySelector('.links');
  if(!menu) return;
  const open = menu.classList.toggle('open');
  if(button) button.setAttribute('aria-expanded', String(open));
}

function completeQuote(form){
  const success = form.querySelector('.success');
  const nameValue = form.querySelector('[name="name"]')?.value.trim();
  const first = nameValue ? nameValue.split(/\s+/)[0] : 'there';
  if(success){
    success.style.display = 'block';
    success.textContent = `Thanks, ${first}. Your request is in. Terramorph will follow up to learn more, answer questions, and schedule a free estimate.`;
  }
  const btn = form.querySelector('button[type="submit"]');
  if(btn) btn.textContent = 'Request Sent ✓';
  window.localStorage?.setItem('terramorphQuotePopupSubmitted', '1');
}

function handleQuote(event){
  event.preventDefault();
  completeQuote(event.currentTarget);
}

function openQuotePopup(){
  const popup = document.querySelector('#quote-popup');
  if(!popup || popup.dataset.opened === 'true') return;
  if(window.localStorage?.getItem('terramorphQuotePopupSubmitted') === '1') return;
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
  document.querySelectorAll('.quote-form').forEach(form => form.addEventListener('submit', handleQuote));
  document.querySelectorAll('.links a').forEach(link => link.addEventListener('click', () => {
    const menu = document.querySelector('.links');
    const button = document.querySelector('.mobile-menu');
    menu?.classList.remove('open');
    button?.setAttribute('aria-expanded', 'false');
  }));

  document.querySelectorAll('[data-close-popup]').forEach(el => el.addEventListener('click', closeQuotePopup));
  document.addEventListener('keydown', event => {
    if(event.key === 'Escape') closeQuotePopup();
  });

  // Shows after 12 seconds: inside the 10–15 second range, late enough to avoid feeling instant/spammy.
  window.setTimeout(openQuotePopup, 12000);
});
