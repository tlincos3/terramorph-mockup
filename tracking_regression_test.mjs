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

function adsConversions(harness) {
  return harness.ga4Events.filter(args => args[0] === 'event' && args[1] === 'conversion');
}

function ga4Leads(harness) {
  return harness.ga4Events.filter(args => args[0] === 'event' && args[1] === 'generate_lead');
}

// Thank-you page reached without an on-page submit (hosted request page or an
// old link): one diagnostic, one Meta Lead, one Ads conversion for a Google click.
{
  const harness = buildHarness({
    search: '?utm_source=google&utm_medium=cpc&gclid=current-google-click',
    storedAttribution: {
      utm_source: 'facebook',
      fbclid: 'older-meta-click',
      fbc: 'fb.1.1.older-meta-click'
    }
  });
  evaluate(harness, 'persistTrackingContext(); trackAttributedThankYouView(); trackAttributedThankYouView();');
  assert.equal(
    harness.window.dataLayer.filter(event => event.event === 'quote_thank_you_attributed').length,
    1,
    'The thank-you diagnostic should be recorded once per session.'
  );
  // Since 2026-09-09 every submission is sent to Meta (it does its own matching).
  assert.equal(metaLeadEvents(harness).length, 1, 'One Meta Lead per session on the thank-you page.');
  assert.equal(adsConversions(harness).length, 1, 'One Google Ads conversion for a Google click.');
  assert.equal(adsConversions(harness)[0][2].send_to, 'AW-17691366114/obvlCJaFougcEOKl8_NB');
  assert.equal(ga4Leads(harness).length, 0, 'The thank-you page must not send a GA4 lead of its own.');
}

// Right Hand request form: its "submitted" signal fires each conversion exactly
// once per session, and the thank-you page stays quiet afterwards.
{
  const harness = buildHarness({
    search: '?utm_source=facebook&utm_medium=paid_social&utm_campaign=meta_priority_services_202608&fbclid=current-meta-click&gclid=also-a-google-click'
  });
  evaluate(harness, `persistTrackingContext();
    handleRequestFormEvent({detail: {stage: 'finished', booked: false}});`);
  assert.equal(metaLeadEvents(harness).length, 0, 'Only the submitted stage counts as a lead.');
  evaluate(harness, `
    handleRequestFormEvent({detail: {stage: 'submitted', service: 'Drainage'}});
    handleRequestFormEvent({detail: {stage: 'submitted', service: 'Drainage'}});
    handleRequestFormEvent({detail: {stage: 'booked'}});
    handleRequestFormEvent({detail: {stage: 'finished', booked: true}});
    trackAttributedThankYouView();`);
  assert.equal(adsConversions(harness).length, 1, 'One Google Ads conversion per submitted request.');
  assert.equal(adsConversions(harness)[0][2].send_to, 'AW-17691366114/obvlCJaFougcEOKl8_NB');
  assert.equal(ga4Leads(harness).length, 1, 'One GA4 generate_lead per submitted request.');
  const leads = metaLeadEvents(harness);
  assert.equal(leads.length, 1, 'One Meta Lead per submitted request, none added by thank-you.html.');
  assert.match(leads[0][3].eventID, /^quote-lead-/, 'The Meta Lead carries an event id.');
  assert.equal(
    harness.window.dataLayer.filter(event => event.event === 'quote_request_submitted').length, 1);
  assert.equal(
    harness.window.dataLayer.filter(event => event.event === 'quote_thank_you_attributed').length, 0,
    'thank-you.html must not count a request the form already counted.');
  assert.ok(harness.sessionStorage.getItem('terramorphJobberLeadTracked'));
  assert.equal(
    harness.sessionStorage.getItem('terramorphThankYouLeadTracked'),
    harness.sessionStorage.getItem('terramorphJobberLeadTracked'));
}

// A session that already converted (either guard key set) never counts again.
{
  const harness = buildHarness({search: '?gclid=g1'});
  harness.sessionStorage.setItem('terramorphJobberLeadTracked', 'earlier');
  evaluate(harness, `persistTrackingContext(); handleRequestFormEvent({detail: {stage: 'submitted'}});`);
  assert.equal(adsConversions(harness).length, 0);
  assert.equal(metaLeadEvents(harness).length, 0);
}

// Links to the hosted request page carry the stored campaign details.
{
  const harness = buildHarness({
    search: '?utm_source=facebook&utm_medium=paid_social&utm_campaign=meta_priority_services_202608&utm_content=drainage_v1&fb_campaign_id=101&fb_adset_id=202&fb_ad_id=303&fb_placement=Facebook_Feed&fbclid=current-meta-click'
  });
  const link = {
    value: 'https://app.righthandcrm.com/request/?co=terramorph&service=Drainage+Solutions',
    getAttribute(name) { return name === 'href' ? this.value : null; },
    setAttribute(name, value) { if(name === 'href') this.value = value; }
  };
  harness.context.testLink = link;
  evaluate(harness, 'persistTrackingContext(); decorateTrackingLink(testLink);');
  const decorated = new URL(link.value);
  assert.equal(decorated.searchParams.get('co'), 'terramorph');
  assert.equal(decorated.searchParams.get('service'), 'Drainage Solutions');
  assert.equal(decorated.searchParams.get('utm_campaign'), 'meta_priority_services_202608');
  assert.equal(decorated.searchParams.get('utm_content'), 'drainage_v1');
  assert.equal(decorated.searchParams.get('fb_campaign_id'), '101');
  assert.equal(decorated.searchParams.get('fb_ad_id'), '303');
  assert.equal(decorated.searchParams.get('fbclid'), 'current-meta-click');

  const other = {
    value: 'https://example.com/somewhere',
    getAttribute(name) { return name === 'href' ? this.value : null; },
    setAttribute(name, value) { if(name === 'href') this.value = value; }
  };
  harness.context.otherLink = other;
  evaluate(harness, 'decorateTrackingLink(otherLink);');
  assert.equal(other.value, 'https://example.com/somewhere', 'Other outside links are left alone.');
}

console.log('tracking_regression_test: PASS');
