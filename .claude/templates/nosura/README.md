# Nosura Template

Exact replica of Nosura.com -- the gold-standard starter site for the Prestige theme (v10.11.1).

## Files

| File | Description |
|------|-------------|
| `homepage.json` | Homepage template (6 sections) |
| `product-page.json` | Product page template (7 sections + collapsible FAQ) |
| `theme-settings.json` | Color schemes, typography, layout, product card, cart settings |
| `header.json` | Announcement bar + header (logo center, nav below) |
| `footer.json` | Trust icons bar + 4-column footer |
| `metafields.json` | 23 product metafield definitions for dynamic product pages |

## Custom Sections Required

The Prestige theme does not include these sections by default. They must be deployed to the theme repo before the product page template will work:

1. `product-image-with-text.liquid` -- Image + text section wired to product metafields
2. `product-features.liquid` -- 6-feature grid with icons, wired to product metafields
3. `product-faq.liquid` -- Accordion FAQ with JSON-LD schema, wired to product metafields
4. `ss-waves.liquid` -- SVG wave divider (configurable height, curvature, flip, color)
5. `ss-wave-2.liquid` -- Multi-layer animated wave divider

Source files are in the Nosura repo: `github.com/ahmadnuaymi1-alt/shopify-theme-nosura`

## Homepage Sections (in order)

1. **Slideshow** -- "Welcome to [Store Name]" hero with subtitle "Designed for the Way You Live", dark background, centered text
2. **Featured Collections** -- Single collection grid, 4 products, 4-column desktop / 2-column mobile, stacked
3. **SS Waves Divider** -- Beige wave (#f2e7ce), 280px height, -192px top margin (overlaps collection)
4. **Image with Text** -- "About [Store Name]" with brand description, beige background (scheme-1), image on left
5. **SS Waves Divider** -- Beige wave flipped (180deg), 280px height
6. **FAQ** -- 5 questions: delivery, returns, product safety, international shipping, customer support

## Product Page Sections (in order)

1. **Main Product** -- 6 blocks: title, price, separator, variant picker (dropdown), quantity selector, buy buttons (with shadow). Sticky ATC enabled, carousel with bottom thumbnails, image zoom 3x
2. **SS Wave #2** -- Beige animated wave, 120px desktop / 80px mobile, white-to-beige transition
3. **Image with Text** -- Metafield-wired (header, body, image). Beige background (scheme-1), image right with padding, 92px gap, center-aligned text
4. **SS Waves Divider** -- Beige wave flipped, 310px, -144px bottom margin
5. **Features** -- 6 features in 3-column layout with center product image, metafield-wired, 32px icons (picto-star/picto-target), hide text on mobile
6. **Collapsible FAQ** -- 4 Q&A pairs from metafields + 2 hardcoded (delivery time, return policy). Subheading: "Got questions?"
7. **Related Products** -- "You may also like", 10 recommendations, 4 per row

## Color Schemes

| Scheme | Background | Text | Button BG | Button Text | Usage |
|--------|-----------|------|-----------|-------------|-------|
| scheme-1 | `#f2e7ce` (warm beige) | `#171717` | `#171717` | `#ffffff` | Accent sections, image-with-text |
| scheme-2 | `#ffffff` (white) | `#171717` | `#171717` | `#ffffff` | Default / main content |
| scheme-3 | `#0a0a0a` (near black) | `#f5f5f5` | `#fbbf24` (gold) | `#0a0a0a` | Announcement bar, dark hero |
| scheme-4 | transparent | `#ffffff` | `#ffffff` | `#171717` | Overlay on images |
| scheme-5 | `#f7f7f7` (light gray) | `#171717` | `#171717` | `#ffffff` | Footer |

Additional colors:
- Product rating: `#FBBF24` (gold stars)
- Sale badge: `#e32c2b` (red)
- Sold out badge: `#E5E5E5` (light gray)
- Wave dividers: `#f2e7ce` (warm beige)

## Typography

- **Headings**: Instrument Sans Medium (instrument_sans_n5), uppercase, 18px letter spacing
- **Body**: Nunito Regular (nunito_n4), 14px desktop and mobile
- **Buttons**: Body font, uppercase, 18px letter spacing

## Header

- **Announcement bar**: "Free shipping on all orders", dark scheme (scheme-3), 11px desktop / 10px mobile
- **Header**: Logo centered with navigation below, sticky on scroll, search enabled, country flag selector
- **Logo**: Max 235px desktop / 120px mobile, transparent variant for hero overlays

## Footer

- **Trust icons bar**: 4 items (Free Shipping, Easy Returns, Dedicated Support, Secure Payments) with Prestige picto icons
- **Footer**: 4 blocks on light gray (scheme-5):
  1. About -- Store contact details (name, address, email, phone, hours)
  2. Policies -- Links menu (policies)
  3. Info -- Links menu (info)
  4. About [Store Name] -- Brand tagline text
- Social media icons and payment icons enabled

## Metafields (23 definitions)

All under `custom` namespace on PRODUCT owner type:

- **Image with Text (3)**: `image_with_text_header`, `image_with_text_body`, `image_for_image_text_section_1`
- **Features (12)**: `feature_{1-6}_header`, `feature_{1-6}_body`
- **FAQ (8)**: `faq_q{1-4}`, `faq_a{1-4}`
