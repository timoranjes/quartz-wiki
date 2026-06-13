# Automated Web QA / Pre-Deploy Testing: Best Practices

## 1. Playwright Test Patterns for Single-File HTML Apps

### Configuration Setup

```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },

  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'mobile-chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'mobile-safari',
      use: { ...devices['iPhone 13'] },
    },
  ],

  webServer: {
    command: 'npx serve . -p 3000',
    port: 3000,
    reuseExistingServer: !process.env.CI,
  },
});
```

### Selector Strategies for Single-File Apps

**Data Attributes (Recommended):**
```html
<!-- HTML -->
<button data-testid="submit-btn">Submit</button>
<input data-testid="email-input" type="email" />
<div data-testid="error-message">Error occurred</div>
```

```typescript
// Test
await page.getByTestId('submit-btn').click();
await page.getByTestId('email-input').fill('test@example.com');
await expect(page.getByTestId('error-message')).toBeVisible();
```

**Role-Based Selectors (Accessibility-First):**
```typescript
// Buttons
await page.getByRole('button', { name: 'Submit' }).click();
await page.getByRole('button', { name: /cancel/i }).click();

// Links
await page.getByRole('link', { name: 'Home' }).click();

// Form elements
await page.getByRole('textbox', { name: 'Email' }).fill('test@example.com');
await page.getByRole('checkbox', { name: 'Accept terms' }).check();

// Headings
await expect(page.getByRole('heading', { name: 'Welcome' })).toBeVisible();
```

**Text Selectors:**
```typescript
await page.getByText('Welcome to our site').click();
await page.getByText('Submit', { exact: true }).click();
await page.getByText(/error/i).toBeVisible();
```

### Core Test Patterns

**Basic Interaction Pattern:**
```typescript
import { test, expect } from '@playwright/test';

test('form submission with validation', async ({ page }) => {
  await page.goto('/');
  
  // Fill form
  await page.getByRole('textbox', { name: 'Email' }).fill('invalid-email');
  await page.getByRole('button', { name: 'Submit' }).click();
  
  // Assert validation error
  await expect(page.getByText('Invalid email format')).toBeVisible();
  
  // Fix and resubmit
  await page.getByRole('textbox', { name: 'Email' }).fill('valid@example.com');
  await page.getByRole('button', { name: 'Submit' }).click();
  
  // Assert success
  await expect(page.getByText('Form submitted successfully')).toBeVisible();
});
```

**Async Operation Pattern:**
```typescript
test('handles async loading', async ({ page }) => {
  await page.goto('/');
  
  // Wait for loading state
  await expect(page.getByText('Loading...')).toBeVisible();
  
  // Wait for content to load
  await expect(page.getByRole('heading', { name: 'Content Loaded' })).toBeVisible({
    timeout: 10000,
  });
  
  // Verify content is interactive
  await page.getByRole('button', { name: 'Action' }).toBeEnabled();
});
```

**Network Request Mocking:**
```typescript
test('mocks API responses', async ({ page }) => {
  // Mock successful response
  await page.route('**/api/data', route =>
    route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({ items: ['Item 1', 'Item 2'] }),
    })
  );
  
  await page.goto('/');
  await expect(page.getByText('Item 1')).toBeVisible();
});

test('handles API errors', async ({ page }) => {
  await page.route('**/api/data', route =>
    route.fulfill({
      status: 500,
      body: 'Internal Server Error',
    })
  );
  
  await page.goto('/');
  await expect(page.getByText('Failed to load data')).toBeVisible();
});
```

**Visual Regression Testing:**
```typescript
test('visual regression - homepage', async ({ page }) => {
  await page.goto('/');
  
  // Full page screenshot
  await expect(page).toHaveScreenshot('homepage.png', {
    maxDiffPixelRatio: 0.01,
  });
  
  // Component-specific screenshot
  await expect(page.getByTestId('hero-section')).toHaveScreenshot('hero.png');
});

test('visual regression - mobile', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveScreenshot('homepage-mobile.png', {
    fullPage: true,
    maxDiffPixelRatio: 0.02,
  });
});
```

**Accessibility Testing:**
```typescript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('accessibility compliance', async ({ page }) => {
  await page.goto('/');
  
  const accessibilityScanResults = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
    .analyze();
  
  expect(accessibilityScanResults.violations).toEqual([]);
});

test('keyboard navigation', async ({ page }) => {
  await page.goto('/');
  
  // Tab through interactive elements
  await page.keyboard.press('Tab');
  await expect(page.getByRole('link').first()).toBeFocused();
  
  await page.keyboard.press('Tab');
  await expect(page.getByRole('button').first()).toBeFocused();
  
  // Activate with Enter
  await page.keyboard.press('Enter');
  await expect(page.getByText('Button activated')).toBeVisible();
});
```

**State Management Testing:**
```typescript
test('preserves state across navigation', async ({ page }) => {
  await page.goto('/');
  
  // Set state
  await page.getByRole('textbox', { name: 'Search' }).fill('test query');
  await page.getByRole('link', { name: 'About' }).click();
  await page.getByRole('link', { name: 'Home' }).click();
  
  // Verify state preserved
  await expect(page.getByRole('textbox', { name: 'Search' })).toHaveValue('test query');
});

test('localStorage persistence', async ({ page }) => {
  await page.goto('/');
  
  // Set localStorage
  await page.evaluate(() => {
    localStorage.setItem('theme', 'dark');
  });
  
  // Reload and verify
  await page.reload();
  const theme = await page.evaluate(() => localStorage.getItem('theme'));
  expect(theme).toBe('dark');
  
  // Verify visual state
  await expect(page.locator('body')).toHaveClass(/dark-mode/);
});
```

### Advanced Patterns

**Parallel Test Execution:**
```typescript
test.describe.configure({ mode: 'parallel' });

test('test 1', async ({ page }) => { /* ... */ });
test('test 2', async ({ page }) => { /* ... */ });
test('test 3', async ({ page }) => { /* ... */ });
```

**Test Fixtures:**
```typescript
// fixtures.ts
import { test as base } from '@playwright/test';

export const test = base.extend<{ loggedInPage: Page }>({
  loggedInPage: async ({ page }, use) => {
    await page.goto('/login');
    await page.getByRole('textbox', { name: 'Username' }).fill('testuser');
    await page.getByRole('button', { name: 'Login' }).click();
    await use(page);
  },
});

// test.spec.ts
import { test } from './fixtures';

test('dashboard access', async ({ loggedInPage }) => {
  await loggedInPage.goto('/dashboard');
  await expect(loggedInPage.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
});
```

**Retry and Timeout Configuration:**
```typescript
test('flaky operation with retries', async ({ page }) => {
  test.setTimeout(60000);
  test.retries(3);
  
  await page.goto('/');
  await page.getByRole('button', { name: 'Start Process' }).click();
  
  // Wait for operation to complete
  await expect(page.getByText('Process complete')).toBeVisible({
    timeout: 30000,
  });
});
```

---

## 2. Pre-Deploy Checklists for Static Sites

### Performance Checks

**Core Web Vitals:**
```bash
# Lighthouse CI
npm install -g lighthouse
lighthouse https://example.com --view

# Or use Lighthouse CI in CI/CD
npx lighthouse-ci autorun
```

**Lighthouse CI Configuration:**
```yaml
# lighthouserc.yml
ci:
  collect:
    url:
      - http://localhost:3000/
      - http://localhost:3000/about
    staticDistDir: './dist'
  assert:
    preset: 'lighthouse:recommended'
    assertions:
      categories:performance:
        - error
        - minScore: 0.9
      categories:accessibility:
        - error
        - minScore: 0.95
      categories:seo:
        - error
        - minScore: 0.9
  upload:
    target: 'temporary-public-storage'
```

**Bundle Size Checks:**
```bash
# Check asset sizes
npx bundlesize

# bundlesize.config.json
{
  "files": [
    {
      "path": "./dist/*.js",
      "maxSize": "50 kB"
    },
    {
      "path": "./dist/*.css",
      "maxSize": "20 kB"
    }
  ]
}
```

**Image Optimization:**
```bash
# Check image sizes
find ./dist -name "*.jpg" -o -name "*.png" | xargs ls -lh | awk '$5 > "500K" {print}'

# Use sharp or squoosh for optimization
npx @squoosh/cli --mozjpeg '{quality:80}' -d dist ./src/images/*.jpg
```

### SEO Validation

**HTML Meta Tags:**
```bash
# Check for required meta tags
grep -q '<meta name="description"' index.html || echo "Missing meta description"
grep -q '<meta name="viewport"' index.html || echo "Missing viewport meta"
grep -q '<title>' index.html || echo "Missing title tag"
grep -q 'og:title' index.html || echo "Missing Open Graph tags"
```

**Sitemap and Robots:**
```bash
# Validate sitemap
curl -s https://example.com/sitemap.xml | xmllint --noout -

# Check robots.txt
curl -s https://example.com/robots.txt | grep -q "Sitemap:" || echo "Missing sitemap reference"
```

**Structured Data:**
```bash
# Validate JSON-LD
npx schema-dts validate ./dist/index.html
```

### Accessibility Audits

**Automated Accessibility Testing:**
```bash
# Pa11y CI
npm install -g pa11y-ci

# .pa11yci.json
{
  "defaults": {
    "timeout": 10000,
    "wait": 500,
    "standard": "WCAG2AA"
  },
  "urls": [
    "http://localhost:3000/",
    "http://localhost:3000/about"
  ]
}

pa11y-ci
```

**axe-core Integration:**
```javascript
// axe-audit.js
const axe = require('axe-core');
const { JSDOM } = require('jsdom');
const fs = require('fs');

const html = fs.readFileSync('./dist/index.html', 'utf8');
const dom = new JSDOM(html);

axe.run(dom.window.document).then(results => {
  if (results.violations.length > 0) {
    console.error('Accessibility violations found:');
    results.violations.forEach(violation => {
      console.error(`- ${violation.id}: ${violation.description}`);
    });
    process.exit(1);
  }
  console.log('No accessibility violations');
});
```

### Link Checking

**Broken Link Detection:**
```bash
# Check internal links
npx broken-link-checker http://localhost:3000 -ro

# Or use linkinator
npx linkinator ./dist --recurse

# Check external links
npx linkinator https://example.com --recurse --skip "mailto:"
```

**HTML Validation:**
```bash
# W3C HTML validator
npx html-validate ./dist/**/*.html

# Or use vnu-jar
java -jar vnu.jar --errors-only ./dist/index.html
```

### CSS Validation

**Stylelint:**
```bash
npx stylelint "./src/**/*.css"

# .stylelintrc.json
{
  "extends": "stylelint-config-standard",
  "rules": {
    "color-no-invalid-hex": true,
    "declaration-block-no-duplicate-properties": true,
    "no-descending-specificity": true
  }
}
```

### Security Headers

**Security Check:**
```bash
# Check security headers (for deployed site)
curl -I https://example.com | grep -E "(Content-Security-Policy|X-Frame-Options|X-Content-Type-Options|Strict-Transport-Security)"

# Generate security headers for static hosting
cat > _headers <<EOF
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
EOF
```

### Asset Optimization

**Minification Check:**
```bash
# Verify HTML is minified
wc -l ./dist/index.html | awk '$1 > 10 {print "HTML not minified"; exit 1}'

# Verify CSS is minified
wc -l ./dist/styles.css | awk '$1 > 10 {print "CSS not minified"; exit 1}'

# Verify JS is minified
wc -l ./dist/script.js | awk '$1 > 10 {print "JS not minified"; exit 1}'
```

**Gzip/Brotli Compression:**
```bash
# Check if assets are compressed (for hosting that supports it)
ls -lh ./dist/*.html ./dist/*.css ./dist/*.js

# Pre-compress for static hosting
gzip -k ./dist/*.html ./dist/*.css ./dist/*.js
brotli -k ./dist/*.html ./dist/*.css ./dist/*.js
```

### Complete Pre-Deploy Script

```bash
#!/bin/bash
set -e

echo "🔍 Running pre-deploy checks..."

# 1. Build check
echo "✓ Build completed"

# 2. HTML validation
echo "Validating HTML..."
npx html-validate ./dist/**/*.html

# 3. Link checking
echo "Checking links..."
npx linkinator ./dist --recurse

# 4. Accessibility audit
echo "Running accessibility audit..."
pa11y-ci

# 5. Lighthouse audit
echo "Running Lighthouse audit..."
npx lighthouse-ci autorun

# 6. Bundle size check
echo "Checking bundle sizes..."
npx bundlesize

# 7. Asset optimization check
echo "Verifying asset optimization..."
find ./dist -name "*.html" -o -name "*.css" -o -name "*.js" | xargs wc -l | awk '$1 > 100 && $2 != "total" {print "Warning: " $2 " may not be minified (" $1 " lines)"}'

# 8. Security headers
echo "Checking security configuration..."
test -f ./dist/_headers && echo "✓ Security headers configured" || echo "⚠ No security headers found"

echo "✅ All pre-deploy checks passed!"
```

---

## 3. Mobile Web Bug Detection

### Touch Event Testing

**Touch Interaction Tests:**
```typescript
import { test, expect } from '@playwright/test';

test('touch interactions work correctly', async ({ page }) => {
  await page.goto('/');
  
  // Tap button
  await page.getByRole('button', { name: 'Menu' }).tap();
  await expect(page.getByTestId('mobile-menu')).toBeVisible();
  
  // Swipe gesture
  await page.touchscreen.tap(100, 100);
  await page.touchscreen.tap(100, 200);
  
  // Long press
  await page.getByRole('button', { name: 'Item' }).dispatchEvent('touchstart');
  await page.waitForTimeout(500);
  await page.getByRole('button', { name: 'Item' }).dispatchEvent('touchend');
});

test('touch targets are appropriately sized', async ({ page }) => {
  await page.goto('/');
  
  // Check all interactive elements have minimum 44x44px touch target
  const touchTargets = await page.evaluate(() => {
    const interactiveElements = document.querySelectorAll('a, button, input, select, textarea, [role="button"]');
    const violations: Array<{element: string, width: number, height: number}> = [];
    
    interactiveElements.forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.width < 44 || rect.height < 44) {
        violations.push({
          element: el.tagName + (el.className ? '.' + el.className.split(' ')[0] : ''),
          width: Math.round(rect.width),
          height: Math.round(rect.height),
        });
      }
    });
    
    return violations;
  });
  
  expect(touchTargets).toEqual([]);
});
```

**Touch Event Listener Validation:**
```typescript
test('touch event listeners are properly attached', async ({ page }) => {
  await page.goto('/');
  
  const touchListeners = await page.evaluate(() => {
    const elements = document.querySelectorAll('[data-touch-handler]');
    return Array.from(elements).map(el => ({
      selector: el.getAttribute('data-touch-handler'),
      hasTouchStart: typeof (el as any).ontouchstart !== 'undefined',
    }));
  });
  
  expect(touchListeners.length).toBeGreaterThan(0);
});
```

### Viewport Issues Detection

**Viewport Meta Tag Validation:**
```typescript
test('viewport meta tag is correctly configured', async ({ page }) => {
  await page.goto('/');
  
  const viewportMeta = await page.evaluate(() => {
    const meta = document.querySelector('meta[name="viewport"]');
    return meta ? meta.getAttribute('content') : null;
  });
  
  expect(viewportMeta).toBeTruthy();
  expect(viewportMeta).toContain('width=device-width');
  expect(viewportMeta).toContain('initial-scale=1');
  expect(viewportMeta).not.toContain('maximum-scale=1'); // Prevents zoom
  expect(viewportMeta).not.toContain('user-scalable=no'); // Prevents zoom
});

test('content fits viewport on mobile', async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 667 }); // iPhone SE
  await page.goto('/');
  
  const horizontalOverflow = await page.evaluate(() => {
    return document.documentElement.scrollWidth > document.documentElement.clientWidth;
  });
  
  expect(horizontalOverflow).toBe(false);
});
```

**Responsive Breakpoint Testing:**
```typescript
const viewports = [
  { name: 'mobile-small', width: 320, height: 568 },
  { name: 'mobile', width: 375, height: 667 },
  { name: 'mobile-large', width: 414, height: 896 },
  { name: 'tablet', width: 768, height: 1024 },
  { name: 'desktop', width: 1280, height: 720 },
];

for (const viewport of viewports) {
  test(`layout works at ${viewport.name} (${viewport.width}x${viewport.height})`, async ({ page }) => {
    await page.setViewportSize({ width: viewport.width, height: viewport.height });
    await page.goto('/');
    
    // Check for horizontal overflow
    const hasOverflow = await page.evaluate(() => {
      return document.documentElement.scrollWidth > document.documentElement.clientWidth;
    });
    expect(hasOverflow).toBe(false);
    
    // Check main content is visible
    await expect(page.getByRole('main')).toBeVisible();
    
    // Visual regression
    await expect(page).toHaveScreenshot(`layout-${viewport.name}.png`);
  });
}
```

### Overflow Detection

**Horizontal Overflow Scanner:**
```typescript
test('no horizontal overflow on any page', async ({ page }) => {
  const pages = ['/', '/about', '/contact', '/products'];
  
  for (const path of pages) {
    await page.goto(path);
    
    const overflowElements = await page.evaluate(() => {
      const elements = document.querySelectorAll('*');
      const overflowIssues: Array<{
        selector: string;
        scrollWidth: number;
        clientWidth: number;
      }> = [];
      
      elements.forEach(el => {
        if (el.scrollWidth > el.clientWidth + 1) {
          const selector = el.tagName.toLowerCase() + 
            (el.id ? '#' + el.id : '') + 
            (el.className ? '.' + el.className.split(' ').join('.') : '');
          
          overflowIssues.push({
            selector,
            scrollWidth: el.scrollWidth,
            clientWidth: el.clientWidth,
          });
        }
      });
      
      return overflowIssues;
    });
    
    expect(overflowElements, `Overflow found on ${path}`).toEqual([]);
  }
});

test('no content overflow in mobile viewport', async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 667 });
  await page.goto('/');
  
  const overflowCheck = await page.evaluate(() => {
    const body = document.body;
    const html = document.documentElement;
    
    return {
      bodyOverflow: body.scrollWidth > html.clientWidth,
      htmlOverflow: html.scrollWidth > html.clientWidth,
      bodyScrollWidth: body.scrollWidth,
      htmlClientWidth: html.clientWidth,
    };
  });
  
  expect(overflowCheck.bodyOverflow).toBe(false);
  expect(overflowCheck.htmlOverflow).toBe(false);
});
```

**Overflow CSS Validation:**
```typescript
test('containers have proper overflow handling', async ({ page }) => {
  await page.goto('/');
  
  const overflowStyles = await page.evaluate(() => {
    const containers = document.querySelectorAll('.container, .wrapper, .content, main, section');
    
    return Array.from(containers).map(el => {
      const styles = window.getComputedStyle(el);
      return {
        selector: el.className,
        overflowX: styles.overflowX,
        overflowY: styles.overflowY,
        maxWidth: styles.maxWidth,
      };
    });
  });
  
  // Verify containers don't allow unintended horizontal overflow
  overflowStyles.forEach(container => {
    if (container.overflowX === 'visible' && container.maxWidth === 'none') {
      console.warn(`Container ${container.selector} may cause overflow`);
    }
  });
});
```

### Font Scaling Issues

**Text Resize Testing:**
```typescript
test('text remains readable when zoomed', async ({ page }) => {
  await page.goto('/');
  
  // Simulate 200% zoom
  await page.evaluate(() => {
    document.documentElement.style.fontSize = '200%';
  });
  
  // Check text is still visible and not overlapping
  const textElements = await page.evaluate(() => {
    const elements = document.querySelectorAll('p, h1, h2, h3, h4, h5, h6, span, a');
    const issues: Array<{selector: string, issue: string}> = [];
    
    elements.forEach(el => {
      const rect = el.getBoundingClientRect();
      const styles = window.getComputedStyle(el);
      
      // Check for text clipping
      if (rect.height < parseInt(styles.fontSize) * 1.2) {
        issues.push({
          selector: el.tagName.toLowerCase(),
          issue: 'Text may be clipped',
        });
      }
      
      // Check for overlapping text
      const nextSibling = el.nextElementSibling;
      if (nextSibling) {
        const nextRect = nextSibling.getBoundingClientRect();
        if (rect.bottom > nextRect.top) {
          issues.push({
            selector: el.tagName.toLowerCase(),
            issue: 'Text overlapping with next element',
          });
        }
      }
    });
    
    return issues;
  });
  
  expect(textElements).toEqual([]);
});

test('font sizes meet minimum requirements', async ({ page }) => {
  await page.goto('/');
  
  const fontSizes = await page.evaluate(() => {
    const elements = document.querySelectorAll('p, span, a, li, label');
    const smallFonts: Array<{selector: string, fontSize: number}> = [];
    
    elements.forEach(el => {
      const fontSize = parseInt(window.getComputedStyle(el).fontSize);
      if (fontSize < 12) { // Minimum 12px for readability
        smallFonts.push({
          selector: el.tagName.toLowerCase() + (el.className ? '.' + el.className.split(' ')[0] : ''),
          fontSize,
        });
      }
    });
    
    return smallFonts;
  });
  
  expect(fontSizes, 'Found fonts smaller than 12px').toEqual([]);
});

test('relative units used for font sizes', async ({ page }) => {
  await page.goto('/');
  
  const fontUnits = await page.evaluate(() => {
    const stylesheets = Array.from(document.styleSheets);
    const fixedFonts: string[] = [];
    
    stylesheets.forEach(sheet => {
      try {
        const rules = Array.from(sheet.cssRules || []);
        rules.forEach((rule: CSSRule) => {
          if (rule instanceof CSSStyleRule) {
            const fontSize = rule.style.fontSize;
            if (fontSize && (fontSize.includes('px') || fontSize.includes('pt'))) {
              fixedFonts.push(`${rule.selectorText}: ${fontSize}`);
            }
          }
        });
      } catch (e) {
        // Cross-origin stylesheet
      }
    });
    
    return fixedFonts;
  });
  
  // Warn about fixed font sizes (should use rem/em)
  if (fontUnits.length > 0) {
    console.warn('Consider using relative units (rem/em) for better accessibility:');
    fontUnits.forEach(f => console.warn(`  - ${f}`));
  }
});
```

### Mobile-Specific Bug Detection

**iOS Safari Issues:**
```typescript
test('iOS Safari compatibility', async ({ page }) => {
  await page.goto('/');
  
  // Check for -webkit- prefixes where needed
  const webkitIssues = await page.evaluate(() => {
    const stylesheets = Array.from(document.styleSheets);
    const issues: string[] = [];
    
    stylesheets.forEach(sheet => {
      try {
        const rules = Array.from(sheet.cssRules || []);
        rules.forEach((rule: CSSRule) => {
          if (rule instanceof CSSStyleRule) {
            // Check for backdrop-filter without -webkit- prefix
            if (rule.style.backdropFilter && !rule.style.webkitBackdropFilter) {
              issues.push(`${rule.selectorText}: backdrop-filter needs -webkit- prefix`);
            }
            
            // Check for sticky positioning
            if (rule.style.position === 'sticky') {
              issues.push(`${rule.selectorText}: position:sticky may have issues on iOS`);
            }
          }
        });
      } catch (e) {}
    });
    
    return issues;
  });
  
  if (webkitIssues.length > 0) {
    console.warn('iOS Safari compatibility issues:');
    webkitIssues.forEach(issue => console.warn(`  - ${issue}`));
  }
});

test('safe area insets respected', async ({ page }) => {
  await page.goto('/');
  
  const safeAreaCheck = await page.evaluate(() => {
    const elements = document.querySelectorAll('header, footer, .fixed-bottom, .fixed-top');
    const issues: Array<{selector: string, issue: string}> = [];
    
    elements.forEach(el => {
      const styles = window.getComputedStyle(el);
      const paddingTop = styles.paddingTop;
      const paddingBottom = styles.paddingBottom;
      
      // Check if fixed elements use env(safe-area-inset-*)
      if (styles.position === 'fixed') {
        if (!paddingTop.includes('env(') && !paddingTop.includes('constant(')) {
          if (el.tagName === 'HEADER' || el.classList.contains('fixed-top')) {
            issues.push({
              selector: el.className || el.tagName,
              issue: 'Fixed header should use env(safe-area-inset-top)',
            });
          }
        }
        
        if (!paddingBottom.includes('env(') && !paddingBottom.includes('constant(')) {
          if (el.tagName === 'FOOTER' || el.classList.contains('fixed-bottom')) {
            issues.push({
              selector: el.className || el.tagName,
              issue: 'Fixed footer should use env(safe-area-inset-bottom)',
            });
          }
        }
      }
    });
    
    return issues;
  });
  
  expect(safeAreaCheck).toEqual([]);
});
```

**Android Chrome Issues:**
```typescript
test('Android Chrome address bar handling', async ({ page }) => {
  await page.goto('/');
  
  // Check for 100vh issues
  const viewportHeightIssues = await page.evaluate(() => {
    const elements = document.querySelectorAll('[style*="100vh"], .full-height, .vh-100');
    const issues: Array<{selector: string, issue: string}> = [];
    
    elements.forEach(el => {
      const styles = window.getComputedStyle(el);
      if (styles.height === '100vh' || styles.minHeight === '100vh') {
        issues.push({
          selector: el.className || el.tagName,
          issue: '100vh may be incorrect on mobile due to address bar. Consider using dvh or JS fallback',
        });
      }
    });
    
    return issues;
  });
  
  if (viewportHeightIssues.length > 0) {
    console.warn('Viewport height issues detected:');
    viewportHeightIssues.forEach(issue => console.warn(`  - ${issue.selector}: ${issue.issue}`));
  }
});
```

**Touch Scrolling Issues:**
```typescript
test('scrollable areas work on touch devices', async ({ page }) => {
  await page.goto('/');
  
  // Find scrollable containers
  const scrollableAreas = await page.evaluate(() => {
    const elements = document.querySelectorAll('*');
    const scrollable: Array<{
      selector: string;
      overflow: string;
      scrollHeight: number;
      clientHeight: number;
    }> = [];
    
    elements.forEach(el => {
      const styles = window.getComputedStyle(el);
      const isScrollable = 
        (styles.overflow === 'auto' || styles.overflow === 'scroll' ||
         styles.overflowY === 'auto' || styles.overflowY === 'scroll') &&
        el.scrollHeight > el.clientHeight;
      
      if (isScrollable) {
        scrollable.push({
          selector: el.className || el.tagName,
          overflow: styles.overflow || styles.overflowY,
          scrollHeight: el.scrollHeight,
          clientHeight: el.clientHeight,
        });
      }
    });
    
    return scrollable;
  });
  
  // Test each scrollable area
  for (const area of scrollableAreas) {
    const selector = `.${area.selector.split(' ')[0]}`;
    
    // Try to scroll
    await page.evaluate((sel) => {
      const el = document.querySelector(sel);
      if (el) {
        el.scrollTop = el.scrollHeight;
      }
    }, selector);
    
    // Verify scroll worked
    const scrollPosition = await page.evaluate((sel) => {
      const el = document.querySelector(sel);
      return el ? el.scrollTop : 0;
    }, selector);
    
    expect(scrollPosition).toBeGreaterThan(0);
  }
});
```

### Comprehensive Mobile QA Script

```typescript
// mobile-qa.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Mobile QA Suite', () => {
  const mobileViewports = [
    { name: 'iPhone SE', width: 375, height: 667 },
    { name: 'iPhone 13', width: 390, height: 844 },
    { name: 'Pixel 5', width: 393, height: 851 },
    { name: 'iPad', width: 768, height: 1024 },
  ];

  for (const viewport of mobileViewports) {
    test.describe(`${viewport.name} (${viewport.width}x${viewport.height})`, () => {
      test.beforeEach(async ({ page }) => {
        await page.setViewportSize({ width: viewport.width, height: viewport.height });
      });

      test('no horizontal overflow', async ({ page }) => {
        await page.goto('/');
        const hasOverflow = await page.evaluate(() => 
          document.documentElement.scrollWidth > document.documentElement.clientWidth
        );
        expect(hasOverflow).toBe(false);
      });

      test('touch targets are 44x44px minimum', async ({ page }) => {
        await page.goto('/');
        const violations = await page.evaluate(() => {
          const elements = document.querySelectorAll('a, button, input, [role="button"]');
          return Array.from(elements).filter(el => {
            const rect = el.getBoundingClientRect();
            return rect.width < 44 || rect.height < 44;
          }).length;
        });
        expect(violations).toBe(0);
      });

      test('font sizes are readable (≥12px)', async ({ page }) => {
        await page.goto('/');
        const smallFonts = await page.evaluate(() => {
          const elements = document.querySelectorAll('p, span, a, li');
          return Array.from(elements).filter(el => {
            const fontSize = parseInt(window.getComputedStyle(el).fontSize);
            return fontSize < 12;
          }).length;
        });
        expect(smallFonts).toBe(0);
      });

      test('viewport meta tag is correct', async ({ page }) => {
        await page.goto('/');
        const viewportMeta = await page.evaluate(() => {
          const meta = document.querySelector('meta[name="viewport"]');
          return meta ? meta.getAttribute('content') : null;
        });
        expect(viewportMeta).toContain('width=device-width');
        expect(viewportMeta).toContain('initial-scale=1');
      });

      test('visual regression', async ({ page }) => {
        await page.goto('/');
        await expect(page).toHaveScreenshot(`mobile-${viewport.name}.png`, {
          fullPage: true,
        });
      });
    });
  }
});
```

---

## Industry Standard Tools Summary

### Testing Frameworks
- **Playwright** - Modern E2E testing with built-in mobile emulation
- **Cypress** - Alternative E2E framework with good DX
- **Puppeteer** - Lower-level browser automation

### Performance & Quality
- **Lighthouse CI** - Automated performance, accessibility, SEO audits
- **WebPageTest** - Advanced performance testing
- **bundlesize** - Bundle size enforcement

### Accessibility
- **axe-core** - Automated accessibility testing
- **Pa11y** - Accessibility testing CLI
- **WAVE** - Visual accessibility evaluation

### Link & HTML Validation
- **linkinator** - Fast link checking
- **html-validate** - HTML validation
- **broken-link-checker** - Comprehensive link checking

### Visual Regression
- **Playwright screenshots** - Built-in visual testing
- **Percy** - Visual review platform
- **Chromatic** - Visual testing for component libraries

### Mobile-Specific
- **BrowserStack** - Real device testing
- **LambdaTest** - Cross-browser testing
- **Chrome DevTools Device Mode** - Local mobile emulation

### CI/CD Integration
- **GitHub Actions** - Automate all checks in CI
- **GitLab CI** - Alternative CI platform
- **CircleCI** - Popular CI service

---

## Recommended Pre-Deploy Checklist

1. ✅ **Build & Bundle**
   - Build completes without errors
   - Bundle sizes within limits
   - Assets minified and compressed

2. ✅ **Validation**
   - HTML validates without errors
   - CSS validates without errors
   - No broken links (internal or external)

3. ✅ **Accessibility**
   - WCAG 2.1 AA compliance (automated scan)
   - Keyboard navigation works
   - Screen reader compatible

4. ✅ **Performance**
   - Lighthouse scores ≥90 (Performance, Accessibility, SEO)
   - Core Web Vitals pass
   - Images optimized

5. ✅ **Mobile**
   - No horizontal overflow on any viewport
   - Touch targets ≥44x44px
   - Font sizes ≥12px
   - Viewport meta tag correct
   - Safe area insets respected

6. ✅ **Security**
   - Security headers configured
   - No mixed content
   - HTTPS enforced

7. ✅ **SEO**
   - Meta tags present
   - Structured data valid
   - Sitemap generated
   - Robots.txt configured

8. ✅ **Visual**
   - Visual regression tests pass
   - Cross-browser testing complete
   - Mobile layouts verified
