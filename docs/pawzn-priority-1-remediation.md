# Pawzn.shop Priority 1 Remediation Plan

This document converts the Priority 1 audit findings for `www.pawzn.shop` into an implementation checklist that can be applied in Shopify or in the store theme once theme files/admin access are available.

## 1. Standardize customer contact email

Choose one primary public customer-support email and use it everywhere.

Recommended value:

```text
hello@pawzn.shop
```

Replace all public variants, including:

```text
contacto@pawzn.com
contacto@pawzn.shop
support@pawzn.shop
```

Locations to update:

- Footer contact block.
- About page.
- Contact page.
- Refund policy.
- Shipping policy.
- Privacy policy.
- Terms of service.
- Shopify notification templates.
- Product-page trust blocks.
- Structured data or organization schema, if present.

Validation checklist:

- Search the theme and page content for `@pawzn`.
- Confirm only the selected public email appears on customer-facing pages.
- Configure forwarding for old addresses so customer messages are not lost.

## 2. Correct product pricing consistency

Audit all active products and confirm their live prices, compare-at prices, and structured data are aligned.

Known item to verify first:

- `3-in-1 Electric Steam Brush`

Expected public pricing should be internally consistent across:

- Product page.
- Collection cards.
- Home-page featured product cards.
- Cart drawer.
- Checkout.
- Product structured data.
- Merchant Center feed, if used.
- Google indexed snippets.

Implementation checklist:

- In Shopify Admin, open each product and verify `Price` and `Compare-at price`.
- Remove inflated compare-at prices unless they reflect a real prior price.
- Regenerate or resubmit the sitemap after changes.
- Request reindexing of high-priority URLs in Google Search Console.
- If Google Merchant Center is used, fetch the latest feed and resolve price mismatch warnings.

## 3. Rewrite unsupported or risky product claims

Avoid claims that imply medical, behavioral, certification, or lab-tested proof unless the store can show supporting documentation.

### Replace certification claims

Avoid:

```text
Certified BPA-free
Rigorously tested
Non-toxic certified materials
```

Use safer language:

```text
Made with BPA-free materials.
Designed with pet-safe materials for everyday use.
```

Only use `certified`, `tested`, or similar terms if a supplier certificate or lab report is available and can be referenced.

### Replace anxiety and health claims

Avoid:

```text
Reduces anxiety
Reduces bloating and digestive issues
10 minutes of nose work equals a 45-minute walk
```

Use safer language:

```text
May help keep pets occupied during stressful moments.
Designed to encourage slower eating.
Provides mental enrichment through sniffing and foraging.
```

Validation checklist:

- Review every product description.
- Review homepage sections.
- Review collection descriptions.
- Review meta titles and meta descriptions.
- Review ad copy if paid campaigns are active.

## 4. Complete and align customer policies

The site should clearly support public promises such as free shipping over $50, shipping from Las Vegas, secure checkout, and 30-day returns.

Required policy pages:

- Refund policy.
- Shipping policy.
- Privacy policy.
- Terms of service.
- Contact page.

Refund policy should clearly state:

- Return window length.
- Whether opened or used pet products are eligible.
- Hygiene-related exceptions.
- Whether the customer or store pays return shipping.
- How refunds are processed.
- How long refunds take after approval.
- Required order information for return requests.

Shipping policy should clearly state:

- Processing time.
- Estimated U.S. delivery time.
- Whether orders ship from Las Vegas or another fulfillment location.
- Free-shipping threshold.
- Shipping regions served.
- Lost, delayed, or returned package handling.

Footer checklist:

- Link to Shipping Policy.
- Link to Refund Policy.
- Link to Privacy Policy.
- Link to Terms of Service.
- Show the same support email used elsewhere.

## 5. Remove accidental mixed-language content

If the primary market is the United States and the storefront is in English, keep all customer-facing trust bullets in English.

Replace Spanish snippets such as:

```text
Envío gratis en EE.UU.
Devoluciones en 30 días
Enviamos desde Las Vegas
```

With:

```text
Free U.S. shipping over $50
30-day returns
Ships from Las Vegas
```

If Spanish is a target language, implement a complete Spanish locale instead of mixing languages in English templates.

Validation checklist:

- Search theme and Shopify page content for Spanish strings.
- Review product templates.
- Review reusable trust badges or icon rows.
- Review notification templates.
- Confirm the storefront language is consistent on mobile and desktop.

## Launch validation

After making the live changes, complete this final pass:

- Open the home page, at least one collection page, and every product page.
- Confirm email, pricing, claims, policies, and language are consistent.
- Test add-to-cart and cart drawer messaging.
- Check footer links on desktop and mobile.
- Submit sitemap in Google Search Console.
- Request reindexing for the home page and top product pages.
