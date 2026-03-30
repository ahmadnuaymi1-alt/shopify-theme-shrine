# Empire Template

Starter site template for the Empire theme (v12.2.1) by Pixel Union. Styled to match the Prestige/Nosura warm aesthetic with dark text, clean uppercase headings and a warm cream accent.

## Files

| File | Description |
|------|-------------|
| `homepage.json` | Homepage template (6 sections) |
| `product-page.json` | Product page template (6 sections + metafield-wired custom sections) |
| `theme-settings.json` | Colors, typography, layout, product card, cart settings |
| `header.json` | Announcement bar + header (logo left, nav below) |
| `footer.json` | Trust icons bar + 4-column footer |
| `metafields.json` | 23 product metafield definitions for dynamic product pages |

## Custom Sections Required

Empire does not include these sections by default. They must be deployed to the theme repo before the product page template will work:

1. `product-image-with-text.liquid` — Image + text section wired to product metafields
2. `product-features.liquid` — 6-feature grid with icons, wired to product metafields
3. `product-faq.liquid` — Accordion FAQ with JSON-LD schema, wired to product metafields

## Homepage Sections (in order)

1. **Slideshow** — "Your Trusted Equipment Partner" hero with subtitle, dark overlay, centered text. Image set via theme editor image picker.
2. **Highlights Banner** — 4 trust icons: Authorized Dealer, Free Shipping, Expert Support, Secure Payments
3. **Featured Collection** — Product grid, 4 columns desktop / 2 mobile
4. **Image with Text** — About section with brand story, warm cream background (#f5f3ed). Image set via theme editor image picker.
5. **Testimonials** — Customer reviews carousel
6. **FAQ** — 5 homepage FAQs (delivery, returns, authorized dealer, international, support)

## Product Page Sections (in order)

1. **Main Product** — 9 blocks: title, rating, price, inventory, form, key-details (authorized dealer badge), description, shipping tab, returns tab. Gallery with bottom thumbnails, click-to-zoom.
2. **Image with Text** — Metafield-wired (header, body, image). Warm cream background.
3. **Features** — 6-feature grid, metafield-wired, 3 columns desktop
4. **FAQ** — 4 metafield Q&A pairs + 2 hardcoded fallbacks
5. **Highlights Banner** — Trust icons (same 4 as homepage)
6. **Recommendations** — "You May Also Like" grid

## Color Scheme

Empire uses flat color settings (not Shopify color schemes). Prestige-inspired warm palette:

| Setting | Value | Usage |
|---------|-------|-------|
| `color_background` | `#ffffff` | Main content |
| `color_footer_background` | `#f5f3ed` | Footer, accent sections |
| `color_header_background` | `#ffffff` | Header |
| `color_text` / `color_headings` | `#1d1d1d` | All text |
| `color_links` | `#046e82` | Links, icon accents |
| `color_button_background` | `#1d1d1d` | Primary buttons |
| `color_button_text` | `#ffffff` | Button text |
| `color_product_sale_accent` | `#e32c2b` | Sale badges |
| `color_product_review_star` | `#ffab41` | Star ratings |
| Checkout accent | `#046e82` | Checkout highlights |
| Checkout button | `#1d1d1d` | Checkout button |

## Typography

- **Headings**: Montserrat Bold (montserrat_n7), UPPERCASE, 5% letter spacing
- **Body**: Nunito Sans Regular (nunito_sans_n4), 16px
- **Menu**: Nunito Sans Bold (nunito_sans_n7)
- **Buttons**: Nunito Sans Bold, UPPERCASE, 2% letter spacing

## Header

- **Announcement bar**: "Authorized Dealer — Free Shipping on All Orders", dark background (#1d1d1d), white text
- **Header**: Logo left with navigation below, sticky on scroll, search enabled, country selector

## Footer

- **Trust icons bar**: 4 items on warm cream background (Authorized Dealer, Free Shipping, Dedicated Support, Secure Payments) using Empire built-in icons
- **Footer**: 4 blocks on warm cream (#f5f3ed):
  1. About — Store contact details (name, address, email, phone, hours)
  2. Policies — Links menu (policies)
  3. Info — Links menu (info)
  4. About [Store Name] — Brand tagline text
- Social media icons and payment icons enabled

## Metafields (23 definitions)

All under `custom` namespace on PRODUCT owner type:

- **Image with Text (3)**: `image_with_text_header`, `image_with_text_body`, `image_for_image_text_section_1`
- **Features (12)**: `feature_{1-6}_header`, `feature_{1-6}_body`
- **FAQ (8)**: `faq_q{1-4}`, `faq_a{1-4}`

## Image Handling

All images use theme editor image pickers — NOTHING is hardcoded:
- Slideshow hero: set via slide block image picker
- Image with Text (homepage): set via section image picker
- Image with Text (product): wired to `image_for_image_text_section_1` metafield (file_reference)
- Logo: set via header section image picker
- All promo/collection images: set via theme editor
