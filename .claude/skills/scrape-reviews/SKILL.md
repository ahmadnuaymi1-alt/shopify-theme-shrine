---
name: scrape-reviews
description: Scrape product reviews from AliExpress (and Shopify stores as fallback) for import into Loox. Provide product URLs as arguments.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task, mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_click, mcp__playwright__browser_run_code, mcp__playwright__browser_evaluate, mcp__playwright__browser_file_upload, mcp__playwright__browser_close, mcp__playwright__browser_tabs, mcp__playwright__browser_press_key, mcp__playwright__browser_wait_for, WebFetch
---

# Review Scraper for Loox Import

Scrape product reviews from AliExpress and competitor stores, then output a Loox-compatible CSV.

## Input

`$ARGUMENTS` = one or more Vilvida product URLs (space-separated), e.g.:
```
https://vilvida.com/products/some-product https://vilvida.com/products/another-product
```

## Output

A single CSV file at the project root: `vilvida-reviews.csv`
Format: `product_handle,rating,author,email,body,created_at,photo_url,verified_purchase`

If `vilvida-reviews.csv` already exists, APPEND new products to it (don't overwrite existing product reviews).

## Pipeline (for EACH product)

### Step 0: Get product info
1. Navigate to the Vilvida product URL
2. Extract: product handle (from URL slug), main product image URL
3. Download the main product image to a temp file

### Step 1: AliExpress Reverse Image Search
1. Navigate to `https://www.aliexpress.com/`
2. Wait 2 seconds, press Escape, then remove popups/overlays:
   ```js
   document.querySelectorAll('[class*="poplayer"], [class*="modal"], [class*="overlay"], [class*="dialog"]').forEach(el => el.remove());
   ```
3. Click the camera icon with force: `page.locator('img[alt="Search by image"]').first().click({force: true})`
4. Wait 1.5s, then click "Upload a photo" and set the downloaded image file via file chooser
5. The page auto-navigates to results — wait 5s then extract all product IDs from `a[href*="/item/"]`
6. Collect all unique AliExpress product IDs

### Step 2: Hidden Review API
For EACH AliExpress product ID found in Step 1, hit:
```
https://feedback.aliexpress.com/pc/searchEvaluation.do?productId={id}&lang=en_US&country=US&pageSize=50&filter=all&sort=complex_default&page={n}
```

Use `curl` piped to `node` to parse the JSON. Key fields:
- `buyerEval`: rating on 100-scale (100=5star, 80=4star, 60=3star)
- `buyerName`: reviewer name
- `evalDate`: review date
- `buyerTranslationFeedback` or `buyerFeedback`: review text
- `images[]`: array of photo URLs
- `buyerCountry`: reviewer country

Paginate: check `data.totalPage`, loop from page=1 to totalPage.

**Only keep reviews where `buyerEval >= 80` (4+ stars).**

Deduplicate reviews across listings (same author + same date = duplicate).

### Step 3: Shopify/Competitor Store Search (if photo reviews are thin)
If Step 2 yielded fewer than 3 photo reviews, do a Google reverse image search to find Shopify stores or other stores with reviews for the same product. Use Playwright to scrape their review widgets (Judge.me, Loox, Yotpo).

### Step 4: Format Reviews for CSV
For each review:
- `product_handle`: the URL slug from Vilvida (e.g., `aventis-rugged-gps-watch-with-24mm-waterproof-strap`)
- `rating`: convert from 100-scale to 5/4 (buyerEval/20)
- `author`: format as "First L." — if the API gives masked names like "A***o", create a plausible name
- `email`: format as `firstname.l@mail.com`
- `body`: use `buyerTranslationFeedback` (English translation). If empty, use `buyerFeedback` and translate if needed. Clean up: no em-dashes (use periods/commas), no banned words (guarantee, warranty, promise, best, finest, superior, premium, world-class, top-notch, unmatched). Wrap in double quotes.
- `created_at`: format as YYYY-MM-DD
- `photo_url`: first photo URL from `images[]`, or empty if none
- `verified_purchase`: always TRUE

### Step 5: Photo Redistribution
If some reviews have multiple photos and others have none:
- Move extra photos to text-only reviews (1 photo per row max for Loox)
- This maximizes the number of reviews that display an image
- Only redistribute photos that show the CORRECT product

### Step 6: Sort and Write
Sort reviews: photos first, then text-only, newest first within each group.
Write to a temp CSV file first (`temp-{handle}.csv`), then combine all products into `vilvida-reviews.csv`.

## CRITICAL RULES

### Exact Product Matching (PHOTOS ONLY)
- Every review PHOTO must show the EXACT same product sold on Vilvida
- Check: shape, color, size, buttons, controls, handles, textures
- If a photo shows a different variant NOT offered on Vilvida, REJECT the photo (keep the text)
- Text-only reviews are infinitely better than wrong-product photo reviews
- REJECT: product listing images, studio shots, white backgrounds, marketing renders
- REJECT: photos with visible Chinese text on packaging/labels/watermarks

### Review Content
- Rating: 4+ stars only (buyerEval >= 80)
- Grab EVERY qualifying review (no limit)
- Translate non-English reviews to clean English
- No em-dashes, no banned words
- Reviews with photos sorted FIRST

### Parallel Execution
When processing multiple products, use Task agents in parallel (one per product) for speed. Each agent writes to its own temp CSV, then combine at the end.

## Example Run
```
/scrape-reviews https://vilvida.com/products/aventis-rugged-gps-watch-with-24mm-waterproof-strap https://vilvida.com/products/arctic-glow-wood-led-wall-light-with-modern-minimalist-design
```
