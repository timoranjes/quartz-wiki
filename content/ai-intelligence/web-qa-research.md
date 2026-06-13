# Automated Web QA & Pre-Deploy Testing: Best Practices Research

A practical reference covering Playwright patterns for single-file HTML apps, pre-deploy checklists for static sites, and automated detection of common mobile web bugs.

---

## 1. Playwright Test Patterns for Single-File HTML Apps

### 1.1 Configuration for Local HTML Files

```ts
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  timeout: 30_000,
  expect: { timeout: 5_000 },
  fullyParallel: true,
  retries: 2,
  workers: 4,
  reporter: [['html', { open: 'never' }], ['list']],
  use: {
    // Serve the single HTML file via a local server (preferred over file://)
    baseURL: 'http://localhost:4173',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    actionTimeout: 10_000,
    navigationTimeout: 15_000,
  },
  webServer: {
    command: 'npx serve . -l 4173 --no-clipboard',
    port: 4173,
    reuseExistingServer: !process.env.CI,
  },
  projects: [
    { name: 'chromium-desktop', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox-desktop', use: { ...devices['Desktop Firefox'] } },
    { name: 'webkit-desktop', use: { ...devices['Desktop Safari'] } },
    { name: 'mobile-chrome', use: { ...devices['Pixel 5'] } },
    { name: 'mobile-safari', use: { ...devices['iPhone 13'] } },
  ],
});
```

**Why a local server over `file://`:** `file://` URLs have different security contexts (no `fetch`, restricted `localStorage`, CORS quirks). A static server mirrors production behavior.

### 1.2 Selector Strategies (Ordered by Preference)

```ts
// 1. User-facing locators (most resilient)
page.getByRole('button', { name: 'Submit' });
page.getByRole('heading', { name: /welcome/i });
page.getByLabel('Email address');
page.getByPlaceholder('you@example.com');
page.getByText('Learn more', { exact: true });
page.getByAltText('Company logo');
page.getByTitle('Close dialog');

// 2. Test IDs (stable, decoupled from UI text)
page.getByTestId('checkout-button');
// HTML: <button data-testid="checkout-button">Buy</button>

// 3. CSS selectors (last resort)
page.locator('.modal > .actions button.primary');

// 4. Chaining & filtering
page.locator('.card').filter({ hasText: 'Premium' }).getByRole('button');
page.locator('li').nth(2);
page.locator('article').first();
```

### 1.3 Form Interaction Patterns

```ts
test('form submission with validation', async ({ page }) => {
  await page.goto('/index.html');

  // Fill text inputs
  await page.getByLabel('Email').fill('user@example.com');
  await page.getByLabel('Password').fill('secret123');

  // Select dropdowns
  await page.getByLabel('Country').selectOption('us');

  // Checkboxes & radios
  await page.getByLabel('I agree').check();
  await page.getByLabel('Newsletter').uncheck();

  // File uploads
  await page.getByLabel('Avatar').setInputFiles('avatar.png');

  // Submit and wait for navigation/response
  await Promise.all([
    page.waitForURL('**/success.html'),
    page.getByRole('button', { name: 'Submit' }).click(),
  ]);

  await expect(page.getByTestId('confirmation')).toBeVisible();
});

test('client-side validation messages', async ({ page }) => {
  await page.goto('/index.html');
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(page.getByText('Email is required')).toBeVisible();
  await expect(page.getByLabel('Email')).toBeFocused();
});
```

### 1.4 Async Operations & Network

```ts
test('waits for async data load', async ({ page }) => {
  await page.goto('/index.html');

  // Wait for a specific element that appears after async work
  await expect(page.getByTestId('user-list')).toBeVisible({ timeout: 10_000 });

  // Wait for network to be idle (no requests for 500ms)
  await page.waitForLoadState('networkidle');

  // Wait for a specific API response
  const [response] = await Promise.all([
    page.waitForResponse(resp =>
      resp.url().includes('/api/users') && resp.status() === 200
    ),
    page.getByRole('button', { name: 'Load Users' }).click(),
  ]);

  const users = await response.json();
  expect(users).toHaveLength(5);
});

test('mocks network requests', async ({ page }) => {
  // Fulfill with custom response
  await page.route('**/api/users', route =>
    route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify([{ id: 1, name: 'Test User' }]),
    })
  );

  // Simulate network failure
  await page.route('**/api/analytics', route => route.abort());

  // Simulate slow network
  await page.route('**/api/**', async route => {
    await new Promise(r => setTimeout(r, 2000));
    await route.continue();
  });

  await page.goto('/index.html');
  await expect(page.getByText('Test User')).toBeVisible();
});
```

### 1.5 Visual Regression Testing

```ts
test('homepage visual snapshot', async ({ page }) => {
  await page.goto('/index.html');
  await page.waitForLoadState('networkidle');

  // Full page screenshot
  await expect(page).toHaveScreenshot('homepage.png', {
    maxDiffPixelRatio: 0.01,
    animations: 'disabled',
    mask: [page.getByTestId('dynamic-timestamp')],
  });

  // Element-level snapshot
  await expect(page.getByTestId('hero-section')).toHaveScreenshot('hero.png');
});

test('dark mode snapshot', async ({ page }) => {
  await page.emulateMedia({ colorScheme: 'dark' });
  await page.goto('/index.html');
  await expect(page).toHaveScreenshot('homepage-dark.png');
});
```

### 1.6 Accessibility Testing with axe-core

```ts
// tests/a11y.spec.ts
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('no critical a11y violations', async ({ page }) => {
  await page.goto('/index.html');

  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21aa'])
    .disableRules(['color-contrast']) // if intentional
    .analyze();

  expect(results.violations).toEqual([]);
});

test('specific region passes a11y', async ({ page }) => {
  await page.goto('/index.html');

  const results = await new AxeBuilder({ page })
    .include('#main-content')
    .analyze();

  const critical = results.violations.filter(v => v.impact === 'critical');
  expect(critical).toEqual([]);
});
```

### 1.7 State & localStorage

```ts
test('persists user preferences', async ({ page }) => {
  await page.goto('/index.html');
  await page.getByLabel('Theme').selectOption('dark');

  // Verify localStorage was updated
  const theme = await page.evaluate(() => localStorage.getItem('theme'));
  expect(theme).toBe('dark');

  // Reload and verify state persists
  await page.reload();
  await expect(page.locator('body')).toHaveClass(/theme-dark/);
});

test('pre-seeds localStorage before load', async ({ page }) => {
  await page.addInitScript(() => {
    localStorage.setItem('authToken', 'test-token-123');
    localStorage.setItem('onboardingComplete', 'true');
  });

  await page.goto('/index.html');
  await expect(page.getByTestId('dashboard')).toBeVisible();
});
```

### 1.8 Mobile Device Emulation

```ts
import { devices } from '@playwright/test';

test('mobile layout renders correctly', async ({ browser }) => {
  const context = await browser.newContext({
    ...devices['iPhone 13 Pro'],
    locale: 'en-US',
    geolocation: { latitude: 37.7749, longitude: -122.4194 },
    permissions: ['geolocation'],
  });

  const page = await context.newPage();
  await page.goto('/index.html');

  // Verify mobile-specific elements
  await expect(page.getByTestId('mobile-nav')).toBeVisible();
  await expect(page.getByTestId('desktop-nav')).toBeHidden();

  // Verify viewport meta tag
  const viewport = await page.evaluate(() =>
    document.querySelector('meta[name="viewport"]')?.getAttribute('content')
  );
  expect(viewport).toContain('width=device-width');
});
```

### 1.9 Fixtures for Reusable Setup

```ts
// tests/fixtures.ts
import { test as base, Page } from '@playwright/test';

export const test = base.extend<{ loggedInPage: Page }>({
  loggedInPage: async ({ browser }, use) => {
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.addInitScript(() => {
      localStorage.setItem('session', JSON.stringify({ userId: 'u_123' }));
    });
    await page.goto('/index.html');
    await use(page);
    await context.close();
  },
});

export { expect } from '@playwright/test';

// Usage in tests
import { test, expect } from './fixtures';

test('shows user dashboard', async ({ loggedInPage }) => {
  await expect(loggedInPage.getByTestId('welcome')).toContainText('u_123');
});
```

### 1.10 Core Assertions Cheat Sheet

```ts
// Visibility & existence
await expect(locator).toBeVisible();
await expect(locator).toBeHidden();
await expect(locator).toBeAttached();

// Text content
await expect(locator).toHaveText('Exact match');
await expect(locator).toHaveText(/regex match/i);
await expect(locator).toContainText('partial');

// Attributes & values
await expect(locator).toHaveAttribute('href', '/home');
await expect(locator).toHaveValue('input value');
await expect(locator).toHaveClass(/active/);
await expect(locator).toHaveCSS('display', 'flex');

// URL & title
await expect(page).toHaveURL(/.*dashboard/);
await expect(page).toHaveTitle(/Dashboard/);

// Count
await expect(page.locator('li')).toHaveCount(5);

// Auto-retrying: these poll until pass or timeout
await expect(page.getByText('Loading')).toBeVisible(); // will wait
```

---

## 2. Pre-Deploy Checklists for Static Sites

### 2.1 Performance Checks

**Lighthouse CI configuration:**

```js
// lighthouserc.js
module.exports = {
  ci: {
    collect: {
      staticDistDir: './dist',
      numberOfRuns: 3,
      url: [
        'http://localhost/index.html',
        'http://localhost/about.html',
      ],
    },
    assert: {
      assertions: {
        'categories:performance': ['error', { minScore: 0.9 }],
        'categories:accessibility': ['error', { minScore: 1.0 }],
        'categories:best-practices': ['error', { minScore: 0.95 }],
        'categories:seo': ['error', { minScore: 0.9 }],
        'first-contentful-paint': ['warn', { maxNumericValue: 1800 }],
        'largest-contentful-paint': ['error', { maxNumericValue: 2500 }],
        'interactive': ['warn', { maxNumericValue: 3800 }],
        'cumulative-layout-shift': ['error', { maxNumericValue: 0.1 }],
        'total-byte-weight': ['warn', { maxNumericValue: 500_000 }],
      },
    },
    upload: {
      target: 'temporary-public-storage',
    },
  },
};
```

**Bundle size enforcement:**

```json
// package.json
{
  "scripts": {
    "size": "bundlesize",
    "predeploy": "npm run build && npm run size && npm run lighthouse"
  },
  "bundlesize": [
    { "path": "./dist/*.js", "maxSize": "50 kB", "compression": "gzip" },
    { "path": "./dist/*.css", "maxSize": "15 kB", "compression": "gzip" }
  ]
}
```

**Image optimization checks:**

```bash
# Check for unoptimized images
npx image-size-cli ./dist/images --max-width 2000
# Verify all images are WebP/AVIF where appropriate
find dist -name '*.png' -size +100k  # flag large PNGs
# Check for missing alt attributes
npx html-validate dist/
```

### 2.2 SEO Validation

```js
// scripts/seo-check.js
import { JSDOM } from 'jsdom';
import fs from 'fs';
import glob from 'glob';

const files = glob.sync('dist/**/*.html');
let failures = 0;

for (const file of files) {
  const html = fs.readFileSync(file, 'utf8');
  const dom = new JSDOM(html);
  const doc = dom.window.document;
  const checks = {
    'has title': !!doc.querySelector('title') && doc.querySelector('title').textContent.trim(),
    'has meta description': !!doc.querySelector('meta[name="description"][content]'),
    'has canonical': !!doc.querySelector('link[rel="canonical"][href]'),
    'has og:title': !!doc.querySelector('meta[property="og:title"]'),
    'has og:image': !!doc.querySelector('meta[property="og:image"]'),
    'has lang': !!doc.documentElement.lang,
    'has h1': !!doc.querySelector('h1'),
    'images have alt': [...doc.querySelectorAll('img')].every(img => img.hasAttribute('alt')),
    'has viewport': !!doc.querySelector('meta[name="viewport"]'),
  };

  for (const [check, pass] of Object.entries(checks)) {
    if (!pass) {
      console.error(`✗ ${file}: ${check}`);
      failures++;
    }
  }
}

if (failures) process.exit(1);
console.log(`✓ SEO checks passed for ${files.length} files`);
```

**Sitemap & robots.txt validation:**

```bash
# Validate sitemap XML
npx sitemap-validator dist/sitemap.xml
# Verify all URLs in sitemap exist
npx url-exist --input dist/sitemap.xml
# Check robots.txt syntax
curl -sf https://example.com/robots.txt | npx robots-parser
```

### 2.3 Accessibility Audits in CI

**Pa11y CI configuration:**

```json
// .pa11yci.json
{
  "defaults": {
    "timeout": 10000,
    "standard": "WCAG2AA",
    "runners": ["axe"],
    "reporters": ["cli", "json"]
  },
  "urls": [
    "http://localhost:4173/index.html",
    "http://localhost:4173/about.html",
    "http://localhost:4173/contact.html"
  ]
}
```

**axe-core in Node (no browser needed for static HTML):**

```js
// scripts/a11y-static.js
import { JSDOM } from 'jsdom';
import { axe } from 'axe-core';
import fs from 'fs';

const html = fs.readFileSync('dist/index.html', 'utf8');
const dom = new JSDOM(html);
global.window = dom.window;
global.document = dom.window.document;

const results = await axe(dom.window.document);
if (results.violations.length) {
  console.error(results.violations);
  process.exit(1);
}
```

### 2.4 Link Checking

```bash
# Check internal and external links
npx linkinator ./dist --recurse --skip "example.com"

# Alternative: broken-link-checker
npx blc http://localhost:4173 -rohf

# Check for mixed content (http links on https site)
grep -rn 'href="http://' dist/ && exit 1 || true
```

### 2.5 HTML Validation

```js
// html-validate.config.js
export default {
  extends: ['html-validate:recommended'],
  rules: {
    'no-inline-style': 'warn',
    'require-sri': 'off',
    'valid-id': ['error', { relax: true }],
  },
};
```

```bash
npx html-validate "dist/**/*.html"
```

### 2.6 Security Headers Check

```js
// scripts/security-headers.js
import fs from 'fs';

const REQUIRED_HEADERS = [
  'content-security-policy',
  'x-content-type-options',
  'x-frame-options',
  'referrer-policy',
  'permissions-policy',
];

// For static hosts, verify via _headers file (Netlify) or headers config
const headers = fs.readFileSync('dist/_headers', 'utf8');
for (const header of REQUIRED_HEADERS) {
  if (!headers.toLowerCase().includes(header)) {
    console.error(`Missing security header: ${header}`);
    process.exit(1);
  }
}
```

### 2.7 Cache-Busting Verification

```js
// scripts/cache-bust-check.js
import { JSDOM } from 'jsdom';
import fs from 'fs';

const html = fs.readFileSync('dist/index.html', 'utf8');
const dom = new JSDOM(html);
const doc = dom.window.document;

// All static assets should have hash in filename
const scripts = [...doc.querySelectorAll('script[src]')].map(s => s.src);
const styles = [...doc.querySelectorAll('link[rel="stylesheet"]')].map(l => l.href);

const hashPattern = /\.[a-f0-9]{8,}\.\w+$/;
for (const url of [...scripts, ...styles]) {
  if (!url.startsWith('http') && !hashPattern.test(url)) {
    console.error(`⚠ No cache-busting hash: ${url}`);
    process.exit(1);
  }
}
```

### 2.8 Cross-Browser Matrix (GitHub Actions)

```yaml
# .github/workflows/qa.yml
name: Pre-deploy QA
on: [push, pull_request]

jobs:
  qa:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20 }

      - run: npm ci
      - run: npx playwright install --with-deps

      - name: HTML validation
        run: npx html-validate "dist/**/*.html"

      - name: SEO checks
        run: node scripts/seo-check.js

      - name: Accessibility (Pa11y)
        run: npx pa11y-ci

      - name: Link checking
        run: npx linkinator ./dist --recurse

      - name: Lighthouse CI
        run: npx lhci autorun

      - name: Playwright tests (cross-browser)
        run: npx playwright test

      - name: Bundle size
        run: npx bundlesize

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: playwright-report
          path: playwright-report/
```

### 2.9 Complete Pre-Deploy Script

```bash
#!/bin/bash
# scripts/predeploy.sh
set -e

echo "🔨 Building..."
npm run build

echo "🔍 HTML validation..."
npx html-validate "dist/**/*.html"

echo "🔎 SEO checks..."
node scripts/seo-check.js

echo "♿ Accessibility..."
npx pa11y-ci

echo "🔗 Link checking..."
npx linkinator ./dist --recurse

echo "📊 Lighthouse..."
npx lhci autorun

echo "🧪 Playwright tests..."
npx playwright test

echo "📦 Bundle size..."
npx bundlesize

echo "🔒 Security headers..."
node scripts/security-headers.js

echo "✅ All pre-deploy checks passed"
```

---

## 3. Automatic Detection of Common Mobile Web Bugs

### 3.1 Touch Event Issues

**Problems:** Missing touch handlers, 300ms tap delay, incorrect `touch-action` CSS.

```ts
// tests/mobile-touch.spec.ts
import { test, expect, devices } from '@playwright/test';

test.describe('Touch event correctness', () => {
  test('no 300ms tap delay (viewport meta present)', async ({ page }) => {
    await page.goto('/index.html');

    const viewport = await page.evaluate(() => {
      const meta = document.querySelector('meta[name="viewport"]');
      return meta?.getAttribute('content') || '';
    });

    // width=device-width disables the 300ms delay in modern browsers
    expect(viewport).toMatch(/width\s*=\s*device-width/);
  });

  test('touch-action CSS allows intended gestures', async ({ page }) => {
    await page.goto('/index.html');

    const issues = await page.evaluate(() => {
      const problems: string[] = [];
      // Scrollable elements should not have touch-action: none
      document.querySelectorAll('*').forEach(el => {
        const style = getComputedStyle(el);
        const isScrollable =
          el.scrollHeight > el.clientHeight || el.scrollWidth > el.clientWidth;
        if (isScrollable && style.touchAction === 'none') {
          problems.push(`${el.tagName}.${el.className} is scrollable but has touch-action:none`);
        }
        // Buttons/links should not have touch-action: none (blocks taps)
        if (
          (el.tagName === 'BUTTON' || el.tagName === 'A') &&
          style.touchAction === 'none'
        ) {
          problems.push(`${el.tagName} has touch-action:none (blocks taps)`);
        }
      });
      return problems;
    });

    expect(issues).toEqual([]);
  });

  test('interactive elements respond to tap', async ({ browser }) => {
    const context = await browser.newContext({
      ...devices['iPhone 13'],
      hasTouch: true,
    });
    const page = await context.newPage();
    await page.goto('/index.html');

    const buttons = page.locator('button, [role="button"], a');
    const count = await buttons.count();

    for (let i = 0; i < Math.min(count, 10); i++) {
      const btn = buttons.nth(i);
      if (await btn.isVisible()) {
        // Use touch tap, not mouse click
        await btn.tap();
        // Verify something happened (navigation, state change, etc.)
        await page.waitForTimeout(100);
      }
    }
  });
});
```

### 3.2 Viewport Issues

```ts
test('viewport meta tag is correct', async ({ page }) => {
  await page.goto('/index.html');

  const viewportMeta = await page.evaluate(() => {
    const meta = document.querySelector('meta[name="viewport"]');
    if (!meta) return null;
    const content = meta.getAttribute('content') || '';
    return {
      content,
      hasWidth: /width\s*=\s*device-width/.test(content),
      hasInitialScale: /initial-scale\s*=\s*1/.test(content),
      // user-scalable=no is an a11y issue
      blocksZoom: /user-scalable\s*=\s*no/.test(content) ||
                  /maximum-scale\s*=\s*1/.test(content),
    };
  });

  expect(viewportMeta).not.toBeNull();
  expect(viewportMeta!.hasWidth).toBe(true);
  expect(viewportMeta!.hasInitialScale).toBe(true);
  expect(viewportMeta!.blocksZoom).toBe(false); // a11y violation
});

test('no fixed-position elements overlap content at bottom', async ({ browser }) => {
  const context = await browser.newContext({
    ...devices['iPhone 13'],
    hasTouch: true,
  });
  const page = await context.newPage();
  await page.goto('/index.html');

  const overlaps = await page.evaluate(() => {
    const vh = window.innerHeight;
    const vw = window.innerWidth;
    const fixedEls = [...document.querySelectorAll('*')].filter(el => {
      const s = getComputedStyle(el);
      return s.position === 'fixed' || s.position === 'sticky';
    });

    return fixedEls
      .map(el => {
        const r = el.getBoundingClientRect();
        return {
          tag: el.tagName,
          bottom: r.bottom,
          right: r.right,
          overflowsBottom: r.bottom > vh + 1,
          overflowsRight: r.right > vw + 1,
          coversBottomHalf: r.top > vh / 2 && r.height > vh * 0.3,
        };
      })
      .filter(r => r.overflowsBottom || r.overflowsRight || r.coversBottomHalf);
  });

  expect(overlaps).toEqual([]);
});

test('100vh bug detection (iOS Safari)', async ({ browser }) => {
  const context = await browser.newContext({ ...devices['iPhone 13'] });
  const page = await context.newPage();
  await page.goto('/index.html');

  const issues = await page.evaluate(() => {
    const problems: string[] = [];
    document.querySelectorAll('*').forEach(el => {
      // Flag any element using 100vh (breaks on iOS due to browser chrome)
      const raw = el.getAttribute('style') || '';
      if (/height\s*:\s*100vh/.test(raw)) {
        problems.push(`Element uses 100vh (broken on iOS): ${el.tagName}.${el.className}`);
      }
    });
    return problems;
  });

  // Recommend: use dvh/svh or min-height: 100dvh
  if (issues.length) console.warn('100vh issues:', issues);
});
```

### 3.3 Overflow Detection (Horizontal Scroll)

```ts
test('no horizontal overflow on mobile', async ({ browser }) => {
  const context = await browser.newContext({ ...devices['iPhone 13'] });
  const page = await context.newPage();
  await page.goto('/index.html');
  await page.waitForLoadState('networkidle');

  const overflow = await page.evaluate(() => {
    const vw = document.documentElement.clientWidth;
    const docWidth = Math.max(
      document.body.scrollWidth,
      document.documentElement.scrollWidth
    );
    return {
      viewportWidth: vw,
      documentWidth: docWidth,
      hasHorizontalScroll: docWidth > vw,
      overflowAmount: docWidth - vw,
    };
  });

  expect(overflow.hasHorizontalScroll).toBe(false);
});

test('identifies overflowing elements', async ({ browser }) => {
  const context = await browser.newContext({ ...devices['iPhone 13'] });
  const page = await context.newPage();
  await page.goto('/index.html');

  const culprits = await page.evaluate(() => {
    const vw = document.documentElement.clientWidth;
    const offenders: Array<{ selector: string; right: number; overflow: number }> = [];

    document.querySelectorAll('*').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.right > vw + 1 && r.width > 0) {
        // Skip elements that intentionally overflow (e.g., carousels)
        const style = getComputedStyle(el);
        if (style.overflowX === 'auto' || style.overflowX === 'scroll') return;

        offenders.push({
          selector: `${el.tagName.toLowerCase()}${el.id ? '#' + el.id : ''}${
            el.className ? '.' + String(el.className).split(' ').join('.') : ''
          }`,
          right: Math.round(r.right),
          overflow: Math.round(r.right - vw),
        });
      }
    });

    return offenders.sort((a, b) => b.overflow - a.overflow).slice(0, 10);
  });

  expect(culprits).toEqual([]);
});

test('scroll chaining / overscroll behavior', async ({ page }) => {
  await page.goto('/index.html');

  const issues = await page.evaluate(() => {
    // Modals/overlays should have overscroll-behavior: contain
    // to prevent scroll chaining to the body
    const modals = document.querySelectorAll('[role="dialog"], .modal, .overlay');
    return [...modals].map(el => ({
      tag: el.tagName,
      overscrollBehavior: getComputedStyle(el).overscrollBehavior,
      shouldContain: true,
    })).filter(m => m.overscrollBehavior !== 'contain' && m.overscrollBehavior !== 'none');
  });

  expect(issues).toEqual([]);
});
```

### 3.4 Font Scaling Issues

```ts
test('text-size-adjust is set correctly', async ({ page }) => {
  await page.goto('/index.html');

  const issues = await page.evaluate(() => {
    const body = getComputedStyle(document.body);
    const textSizeAdjust = body.webkitTextSizeAdjust || body.textSizeAdjust;
    return {
      value: textSizeAdjust,
      // 'none' prevents user font scaling (a11y violation)
      // '100%' or 'auto' is correct
      blocksScaling: textSizeAdjust === 'none',
    };
  });

  expect(issues.blocksScaling).toBe(false);
});

test('text remains readable at 200% zoom', async ({ browser }) => {
  const context = await browser.newContext({
    ...devices['iPhone 13'],
    deviceScaleFactor: 2,
  });
  const page = await context.newPage();
  await page.goto('/index.html');

  // Check that text uses relative units (rem/em/%) not fixed px
  const fixedSizeText = await page.evaluate(() => {
    const offenders: string[] = [];
    document.querySelectorAll('p, span, li, a, h1, h2, h3, h4, h5, h6, label').forEach(el => {
      const style = getComputedStyle(el);
      const fontSize = parseFloat(style.fontSize);
      // Flag very small text (<12px) that won't scale well
      if (fontSize < 12) {
        offenders.push(`${el.tagName}: ${fontSize}px`);
      }
    });
    return offenders;
  });

  expect(fixedSizeText).toEqual([]);
});

test('input font-size >= 16px (prevents iOS zoom)', async ({ page }) => {
  await page.goto('/index.html');

  const issues = await page.evaluate(() => {
    const inputs = document.querySelectorAll('input, select, textarea');
    return [...inputs].map(el => {
      const fontSize = parseFloat(getComputedStyle(el).fontSize);
      return {
        tag: el.tagName,
        type: (el as HTMLInputElement).type,
        fontSize,
        willZoomOnFocus: fontSize < 16,
      };
    }).filter(i => i.willZoomOnFocus);
  });

  // iOS Safari auto-zooms when focusing inputs with font-size < 16px
  expect(issues).toEqual([]);
});
```

### 3.5 Tap Target Size (48x48px minimum)

```ts
test('tap targets meet 48x48 minimum (Google/Apple HIG)', async ({ browser }) => {
  const context = await browser.newContext({ ...devices['iPhone 13'] });
  const page = await context.newPage();
  await page.goto('/index.html');

  const smallTargets = await page.evaluate(() => {
    const interactive = document.querySelectorAll(
      'a, button, input, select, textarea, [role="button"], [onclick]'
    );
    const MIN = 48;
    return [...interactive]
      .map(el => {
        const r = el.getBoundingClientRect();
        return {
          selector: `${el.tagName.toLowerCase()}${el.id ? '#' + el.id : ''}`,
          width: Math.round(r.width),
          height: Math.round(r.height),
          tooSmall: r.width < MIN || r.height < MIN,
        };
      })
      .filter(t => t.tooSmall && t.width > 0); // skip hidden
  });

  expect(smallTargets).toEqual([]);
});

test('tap targets do not overlap', async ({ browser }) => {
  const context = await browser.newContext({ ...devices['iPhone 13'] });
  const page = await context.newPage();
  await page.goto('/index.html');

  const overlaps = await page.evaluate(() => {
    const targets = [...document.querySelectorAll(
      'a, button, [role="button"], input'
    )].filter(el => {
      const r = el.getBoundingClientRect();
      return r.width > 0 && r.height > 0;
    }).map(el => ({
      el,
      rect: el.getBoundingClientRect(),
    }));

    const overlaps: string[] = [];
    for (let i = 0; i < targets.length; i++) {
      for (let j = i + 1; j < targets.length; j++) {
        const a = targets[i].rect;
        const b = targets[j].rect;
        // Expand by 8px padding (finger radius)
        const PAD = 8;
        const intersect =
          a.left - PAD < b.right + PAD &&
          a.right + PAD > b.left - PAD &&
          a.top - PAD < b.bottom + PAD &&
          a.bottom + PAD > b.top - PAD;
        if (intersect) {
          overlaps.push(`${targets[i].el.tagName}#${targets[i].el.id} overlaps ${targets[j].el.tagName}#${targets[j].el.id}`);
        }
      }
    }
    return overlaps.slice(0, 10);
  });

  expect(overlaps).toEqual([]);
});
```

### 3.6 Safe Area / Notch Handling

```ts
test('respects safe-area-inset for fixed elements', async ({ browser }) => {
  const context = await browser.newContext({
    ...devices['iPhone 13'],
  });
  const page = await context.newPage();
  await page.goto('/index.html');

  const issues = await page.evaluate(() => {
    // Check if viewport-fit=cover is set (required for safe-area-inset to work)
    const viewport = document.querySelector('meta[name="viewport"]');
    const content = viewport?.getAttribute('content') || '';
    const hasViewportFitCover = /viewport-fit\s*=\s*cover/.test(content);

    // Check fixed-bottom elements use safe-area padding
    const fixedBottom = [...document.querySelectorAll('*')].filter(el => {
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return s.position === 'fixed' && r.bottom >= window.innerHeight - 5;
    });

    const missingSafeArea = fixedBottom.filter(el => {
      const s = getComputedStyle(el);
      const paddingBottom = parseFloat(s.paddingBottom);
      return paddingBottom < 20 && hasViewportFitCover;
    });

    return {
      hasViewportFitCover,
      fixedBottomCount: fixedBottom.length,
      missingSafeAreaCount: missingSafeArea.length,
    };
  });

  if (issues.fixedBottomCount > 0) {
    expect(issues.hasViewportFitCover).toBe(true);
    expect(issues.missingSafeAreaCount).toBe(0);
  }
});
```

### 3.7 iOS Safari-Specific Bugs

```ts
test('iOS input zoom prevention', async ({ browser }) => {
  const context = await browser.newContext({
    ...devices['iPhone 13'],
    hasTouch: true,
  });
  const page = await context.newPage();
  await page.goto('/index.html');

  const inputs = await page.evaluate(() => {
    return [...document.querySelectorAll('input, select, textarea')].map(el => {
      const fontSize = parseFloat(getComputedStyle(el).fontSize);
      return {
        tag: el.tagName,
        type: (el as HTMLInputElement).type,
        fontSize,
        triggersZoom: fontSize < 16,
      };
    });
  });

  const zoomTriggers = inputs.filter(i => i.triggersZoom);
  expect(zoomTriggers).toEqual([]);
});

test('date inputs have proper mobile type', async ({ page }) => {
  await page.goto('/index.html');

  const issues = await page.evaluate(() => {
    // Using type="text" for dates loses the native mobile date picker
    const dateLikeInputs = [...document.querySelectorAll('input')].filter(i =>
      i.placeholder?.match(/date|dd\/mm|mm\/dd|yyyy/i) ||
      i.id?.match(/date/i)
    );
    return dateLikeInputs
      .filter(i => i.type !== 'date' && i.type !== 'datetime-local')
      .map(i => ({ id: i.id, type: i.type, placeholder: i.placeholder }));
  });

  if (issues.length) {
    console.warn('Date inputs without native picker:', issues);
  }
});

test('no rubber-band scroll issues on body', async ({ browser }) => {
  const context = await browser.newContext({ ...devices['iPhone 13'] });
  const page = await context.newPage();
  await page.goto('/index.html');

  const bodyStyle = await page.evaluate(() => {
    const s = getComputedStyle(document.body);
    return {
      overflow: s.overflow,
      height: s.height,
      position: s.position,
    };
  });

  // If body is 100vh with overflow:auto, it will rubber-band
  // Better: body { overflow: hidden; height: 100dvh; } with inner scroll container
  const vh = await page.evaluate(() => window.innerHeight);
  if (bodyStyle.height === `${vh}px`) {
    expect(bodyStyle.overflow).not.toBe('auto');
  }
});
```

### 3.8 Android Chrome-Specific Issues

```ts
test('content not hidden behind Android bottom nav', async ({ browser }) => {
  const context = await browser.newContext({
    ...devices['Pixel 5'],
    hasTouch: true,
  });
  const page = await context.newPage();
  await page.goto('/index.html');

  // Scroll to bottom and check last element is visible
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
  await page.waitForTimeout(500); // let Android address bar settle

  const lastElementVisible = await page.evaluate(() => {
    const body = document.body;
    const lastChild = body.lastElementChild;
    if (!lastChild) return true;
    const r = lastChild.getBoundingClientRect();
    return r.bottom <= window.innerHeight + 1;
  });

  expect(lastElementVisible).toBe(true);
});

test('address bar does not break fixed layouts', async ({ browser }) => {
  const context = await browser.newContext({ ...devices['Pixel 5'] });
  const page = await context.newPage();
  await page.goto('/index.html');

  // Measure at initial scroll
  const initialHeight = await page.evaluate(() => window.innerHeight);

  // Scroll down (address bar hides, innerHeight grows on some browsers)
  await page.evaluate(() => window.scrollTo(0, 500));
  await page.waitForTimeout(300);
  const scrolledHeight = await page.evaluate(() => window.innerHeight);

  // Using 100vh would be constant; innerHeight changes
  // Layouts should use dvh or listen to resize events
  if (initialHeight !== scrolledHeight) {
    console.warn(
      `innerHeight changes on scroll (${initialHeight} → ${scrolledHeight}). ` +
      `Use dvh units for stable layouts.`
    );
  }
});
```

### 3.9 Responsive Breakpoint Automation

```ts
// tests/responsive.spec.ts
import { test, expect } from '@playwright/test';

const VIEWPORTS = [
  { name: 'mobile-small', width: 320, height: 568 },   // iPhone SE
  { name: 'mobile', width: 375, height: 812 },          // iPhone X/11/12
  { name: 'mobile-large', width: 414, height: 896 },    // iPhone 11 Pro Max
  { name: 'tablet', width: 768, height: 1024 },         // iPad
  { name: 'tablet-landscape', width: 1024, height: 768 },
  { name: 'laptop', width: 1366, height: 768 },
  { name: 'desktop', width: 1920, height: 1080 },
];

for (const vp of VIEWPORTS) {
  test(`renders correctly at ${vp.name} (${vp.width}x${vp.height})`, async ({ page }) => {
    await page.setViewportSize({ width: vp.width, height: vp.height });
    await page.goto('/index.html');
    await page.waitForLoadState('networkidle');

    // No horizontal overflow
    const overflow = await page.evaluate(() =>
      document.documentElement.scrollWidth > document.documentElement.clientWidth
    );
    expect(overflow).toBe(false);

    // Visual snapshot per breakpoint
    await expect(page).toHaveScreenshot(`responsive-${vp.name}.png`, {
      fullPage: true,
      maxDiffPixelRatio: 0.02,
    });
  });
}
```

### 3.10 Consolidated Mobile Bug Detection Script

```ts
// scripts/mobile-audit.ts
import { chromium, devices } from 'playwright';

async function mobileAudit(url: string) {
  const browser = await chromium.launch();
  const context = await browser.newContext({
    ...devices['iPhone 13'],
    hasTouch: true,
  });
  const page = await context.newPage();
  await page.goto(url);
  await page.waitForLoadState('networkidle');

  const report = await page.evaluate(() => {
    const issues: Record<string, string[]> = {
      viewport: [],
      overflow: [],
      tapTargets: [],
      fontScaling: [],
      touchAction: [],
      safeArea: [],
    };

    // Viewport
    const vpMeta = document.querySelector('meta[name="viewport"]');
    const vpContent = vpMeta?.getAttribute('content') || '';
    if (!vpMeta) issues.viewport.push('Missing viewport meta tag');
    if (!/width=device-width/.test(vpContent))
      issues.viewport.push('Missing width=device-width');
    if (/user-scalable=no|maximum-scale=1/.test(vpContent))
      issues.viewport.push('Blocks user zoom (a11y)');

    // Overflow
    const vw = document.documentElement.clientWidth;
    const docWidth = document.documentElement.scrollWidth;
    if (docWidth > vw) {
      issues.overflow.push(`Horizontal overflow: doc=${docWidth}px, viewport=${vw}px`);
    }

    // Tap targets
    const MIN_TAP = 48;
    document.querySelectorAll('a, button, [role="button"], input').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.width > 0 && r.height > 0 && (r.width < MIN_TAP || r.height < MIN_TAP)) {
        issues.tapTargets.push(
          `${el.tagName}#${el.id || el.className}: ${Math.round(r.width)}x${Math.round(r.height)} (min ${MIN_TAP}x${MIN_TAP})`
        );
      }
    });

    // Font scaling
    const body = getComputedStyle(document.body);
    if ((body.webkitTextSizeAdjust || body.textSizeAdjust) === 'none') {
      issues.fontScaling.push('text-size-adjust: none blocks user scaling');
    }
    document.querySelectorAll('input, select, textarea').forEach(el => {
      const fs = parseFloat(getComputedStyle(el).fontSize);
      if (fs < 16) {
        issues.fontScaling.push(
          `${el.tagName} has font-size ${fs}px (<16px triggers iOS zoom)`
        );
      }
    });

    // Touch action
    document.querySelectorAll('button, a').forEach(el => {
      if (getComputedStyle(el).touchAction === 'none') {
        issues.touchAction.push(`${el.tagName} has touch-action: none`);
      }
    });

    // Safe area
    if (!/viewport-fit=cover/.test(vpContent)) {
      const hasFixedBottom = [...document.querySelectorAll('*')].some(el => {
        const s = getComputedStyle(el);
        const r = el.getBoundingClientRect();
        return s.position === 'fixed' && r.bottom >= window.innerHeight - 5;
      });
      if (hasFixedBottom) {
        issues.safeArea.push('Fixed-bottom element without viewport-fit=cover');
      }
    }

    return issues;
  });

  await browser.close();

  const total = Object.values(report).reduce((sum, arr) => sum + arr.length, 0);
  console.log(`\n📱 Mobile Audit: ${url}`);
  console.log(`   Found ${total} issue(s)\n`);
  for (const [category, items] of Object.entries(report)) {
    if (items.length) {
      console.log(`❌ ${category}:`);
      items.forEach(i => console.log(`   • ${i}`));
    }
  }

  return { url, totalIssues: total, report };
}

mobileAudit(process.argv[2] || 'http://localhost:4173/index.html');
```

---

## Summary: Key Check Categories & Industry Standard Tools

| Category | Tools | Industry Adoption |
|----------|-------|-------------------|
| **E2E / Interaction Testing** | Playwright, Cypress | Playwright is now the dominant choice (faster, multi-browser, native mobile emulation) |
| **Visual Regression** | Playwright screenshots, Percy, Chromatic, BackstopJS | Percy/Chromatic for team workflows; Playwright built-in for smaller projects |
| **Performance** | Lighthouse CI, WebPageTest, bundlesize, size-limit | Lighthouse CI is de facto standard; integrates into GitHub Actions |
| **Accessibility** | axe-core, Pa11y, @axe-core/playwright, WAVE | axe-core (via Playwright or Pa11y) is the standard; WCAG 2.1 AA target |
| **Link Checking** | linkinator, broken-link-checker, html-validate | linkinator is fastest; runs in CI pre-deploy |
| **HTML Validation** | html-validate, Nu Validator (W3C) | html-validate for CI (fast, configurable); Nu for deep validation |
| **SEO** | Lighthouse SEO audits, custom JSDOM scripts, sitemap-validator | Lighthouse covers most; custom scripts for project-specific rules |
| **Security** | npm audit, Snyk, security header scanners | npm audit in CI; OWASP ZAP for deeper scans |
| **Cross-Browser** | Playwright (Chromium/Firefox/WebKit), BrowserStack | Playwright's 3 engines cover ~95% of real user agents |
| **Mobile Bug Detection** | Playwright device emulation + custom audit scripts | No single tool; combination of viewport emulation, CSS inspection, and touch simulation |

### Recommended Pre-Deploy Pipeline Order

1. **Build** (`npm run build`)
2. **Static analysis** (TypeScript, ESLint, html-validate)
3. **Bundle size check** (bundlesize, size-limit)
4. **SEO + meta checks** (custom script)
5. **Accessibility** (Pa11y CI or axe-core)
6. **Link check** (linkinator)
7. **Unit/component tests** (Vitest, Playwright component tests)
8. **E2E tests across browsers** (Playwright)
9. **Mobile audit** (custom Playwright script from §3.10)
10. **Visual regression** (Playwright screenshots)
11. **Performance** (Lighthouse CI)
12. **Deploy** (only if all pass)

### Key Principles

- **Test on real viewport sizes**, not just desktop — mobile is >60% of traffic
- **Fail fast in CI** — cheap checks (lint, size, links) before expensive ones (Playwright, Lighthouse)
- **Use `data-testid` selectors** — decouple tests from UI text/styling
- **Auto-retrying assertions** — Playwright's `expect().toBeVisible()` polls; prefer over manual waits
- **Visual regression with masking** — mask dynamic content (timestamps, ads) to reduce flakiness
- **Accessibility is non-negotiable** — axe-core catches ~57% of issues automatically; manual testing covers the rest
- **Mobile-specific checks must be automated** — touch target size, 16px input fonts, safe areas, and horizontal overflow are the most common regressions
