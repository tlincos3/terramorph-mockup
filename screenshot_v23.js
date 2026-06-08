const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 1200 }, deviceScaleFactor: 1 });
  await page.goto('http://localhost:8778/index.html', { waitUntil: 'networkidle' });
  await page.screenshot({ path: 'screenshots/home-v2-3-desktop.png', fullPage: true });
  await page.setViewportSize({ width: 390, height: 1200 });
  await page.goto('http://localhost:8778/index.html', { waitUntil: 'networkidle' });
  await page.screenshot({ path: 'screenshots/home-v2-3-mobile.png', fullPage: true });
  await page.setViewportSize({ width: 1440, height: 1200 });
  await page.goto('http://localhost:8778/contact.html', { waitUntil: 'networkidle' });
  await page.screenshot({ path: 'screenshots/contact-v2-3-desktop.png', fullPage: true });
  await browser.close();
})();
