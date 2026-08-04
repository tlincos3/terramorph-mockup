import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
import {fileURLToPath} from 'node:url';

const appPath = new URL('./app.js', import.meta.url);
const appSource = fs.readFileSync(fileURLToPath(appPath), 'utf8');

class MemoryStorage {
  constructor(initial = {}) {
    this.values = new Map(Object.entries(initial));
  }

  getItem(key) {
    return this.values.has(key) ? this.values.get(key) : null;
  }

  setItem(key, value) {
    this.values.set(key, String(value));
  }

  removeItem(key) {
    this.values.delete(key);
  }
}

function buildHarness({search, storedAttribution} = {}) {
  const pageUrl = new URL(`https://terramorphllc.com/thank-you.html${search || ''}`);
  const facebookEvents = [];
  const ga4Events = [];
  const localStorage = new MemoryStorage(
    storedAttribution
      ? {terramorphAttributionContext: JSON.stringify(storedAttribution)}
      : {}
  );
  const sessionStorage = new MemoryStorage();
  const document = {
    activeElement: null,
    body: {classList: {contains: () => false}},
    cookie: '',
    documentElement: {scrollHeight: 1000},
    referrer: '',
    title: 'Quote Request Received | Terramorph',
    addEventListener: () => {},
    querySelector: () => null,
    querySelectorAll: () => []
  };
  const window = {
    dataLayer: [],
    innerHeight: 800,
    innerWidth: 1200,
    localStorage,
    location: {
      href: pageUrl.href,
      origin: pageUrl.origin,
      pathname: pageUrl.pathname,
      search: pageUrl.search
    },
    scrollY: 0,
    sessionStorage,
    addEventListener: () => {},
    setTimeout: () => 0
  };
  const context = vm.createContext({
    console,
    Date,
    FormData,
    Math,
    URL,
    URLSearchParams,
    document,
    window,
    fbq: (...args) => facebookEvents.push(args),
    gtag: (...args) => ga4Events.push(args)
  });
  vm.runInContext(appSource, context, {filename: fileURLToPath(appPath)});
  return {context, facebookEvents, ga4Events, localStorage, sessionStorage, window};
}

function evaluate(harness, expression) {
  return vm.runInContext(expression, harness.context);
}

function metaLeadEvents(harness) {
  return harness.facebookEvents.filter(args => args[0] === 'track' && args[1] === 'Lead');
}

{
  const harness = buildHarness({
    search: '?utm_source=google&utm_medium=cpc&gclid=current-google-click',
    storedAttribution: {
      utm_source: 'facebook',
      fbclid: 'older-meta-click',
      fbc: 'fb.1.1.older-meta-click'
    }
  });
  evaluate(harness, 'persistTrackingContext(); trackAttributedThankYouView();');
  assert.equal(metaLeadEvents(harness).length, 0, 'An explicit Google last-touch source must not be sent to Meta as Lead.');
  assert.equal(
    harness.window.dataLayer.filter(event => event.event === 'quote_thank_you_attributed').length,
    1,
    'The cross-channel thank-you diagnostic should still be recorded once.'
  );
}

{
  const harness = buildHarness({
    search: '?utm_source=facebook&utm_medium=paid_social&utm_campaign=meta_priority_services_202608&utm_content=drainage_v1&fb_campaign_id=101&fb_adset_id=202&fb_ad_id=303&fb_placement=Facebook_Feed&fbclid=current-meta-click'
  });
  evaluate(harness, 'persistTrackingContext(); trackAttributedThankYouView(); trackAttributedThankYouView();');
  assert.equal(metaLeadEvents(harness).length, 1, 'A Meta-attributed Jobber completion should emit one browser Lead per session.');

  const link = {
    value: 'https://clienthub.getjobber.com/client_hubs/1578803/public/work_request/embedded_work_request_form',
    getAttribute(name) { return name === 'href' ? this.value : null; },
    setAttribute(name, value) { if(name === 'href') this.value = value; }
  };
  harness.context.testLink = link;
  evaluate(harness, 'decorateTrackingLink(testLink);');
  const decorated = new URL(link.value);
  assert.equal(decorated.searchParams.get('utm_content'), 'drainage_v1');
  assert.equal(decorated.searchParams.get('fb_campaign_id'), '101');
  assert.equal(decorated.searchParams.get('fb_adset_id'), '202');
  assert.equal(decorated.searchParams.get('fb_ad_id'), '303');
  assert.equal(decorated.searchParams.get('fb_placement'), 'Facebook_Feed');
  assert.equal(decorated.searchParams.get('fbclid'), 'current-meta-click');
}

console.log('tracking_regression_test: PASS');
