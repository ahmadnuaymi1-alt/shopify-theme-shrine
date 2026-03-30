"""Push Empire theme templates to Shopify via Theme Assets API."""

import json
import urllib.request
import time

STORE = "YOUR_STORE.myshopify.com"
TOKEN = "YOUR_SHOPIFY_ACCESS_TOKEN"
THEME_ID = 0  # Replace with your theme ID
API_URL = f"https://{STORE}/admin/api/2024-01/themes/{THEME_ID}/assets.json"


def push_asset(key, value):
    payload = json.dumps({"asset": {"key": key, "value": value}}).encode("utf-8")
    req = urllib.request.Request(API_URL, data=payload, method="PUT")
    req.add_header("X-Shopify-Access-Token", TOKEN)
    req.add_header("Content-Type", "application/json")
    try:
        resp = urllib.request.urlopen(req)
        data = json.loads(resp.read())
        print(f"  OK: {data['asset']['key']}")
        return True
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"  FAIL ({e.code}): {key} - {body}")
        return False


# --- 1. Product page ---
print("1. Pushing product.json...")
product = {
    "sections": {
        "main": {
            "type": "static-product",
            "blocks": {
                "title": {"type": "title", "settings": {}},
                "rating": {"type": "rating", "settings": {}},
                "price": {"type": "price", "settings": {}},
                "inventory": {
                    "type": "inventory_status",
                    "settings": {
                        "inventory_display": "all_products",
                        "inventory_transfer_notice": True,
                    },
                },
                "form": {
                    "type": "form",
                    "settings": {
                        "enable_local_pickup": True,
                        "show_gift_card_recipient_form": False,
                    },
                },
                "key_details": {
                    "type": "key_details",
                    "settings": {
                        "icon": "icon-award-winning",
                        "title": "Authorized Dealer \u2014 Official Product",
                        "text": "<p>This product is sourced directly from the manufacturer. Full brand support included.</p>",
                        "text_color": "#1D1D1D",
                        "icon_color": "#046e82",
                        "background_color": "#f5f3ed",
                    },
                },
                "description": {"type": "description", "settings": {}},
                "tab_shipping": {
                    "type": "collapsible-tab",
                    "settings": {
                        "collapsible_tab_heading": "Shipping Information",
                        "collapsible_tab_text": "<p>We offer free standard shipping on all orders within the United States. Orders are processed within 1 to 2 business days. Estimated delivery is 7 to 10 business days.</p>",
                    },
                },
                "tab_returns": {
                    "type": "collapsible-tab",
                    "settings": {
                        "collapsible_tab_heading": "Returns and Exchanges",
                        "collapsible_tab_text": "<p>We accept returns within 30 days of delivery. Items must be unused and in original packaging. Contact our support team to initiate a return.</p>",
                    },
                },
            },
            "block_order": [
                "title",
                "rating",
                "price",
                "inventory",
                "form",
                "key_details",
                "description",
                "tab_shipping",
                "tab_returns",
            ],
            "settings": {
                "gallery_aspect_ratio": "natural",
                "gallery_image_crop": False,
                "gallery_thumbnail_position": "below",
                "gallery_video_autoplay": True,
                "gallery_video_looping": True,
                "gallery_hover_zoom": "disabled",
                "gallery_click_to_zoom": "always",
            },
        },
        "image_with_text": {
            "type": "product-image-with-text",
            "settings": {
                "heading": "",
                "body": "",
                "image_position": "right",
                "background_color": "#f5f3ed",
                "text_color": "#1d1d1d",
                "padding_top": 60,
                "padding_bottom": 60,
            },
        },
        "features": {
            "type": "product-features",
            "settings": {
                "heading": "Product Highlights",
                "background_color": "#ffffff",
                "text_color": "#1d1d1d",
                "icon_color": "#046e82",
                "columns_desktop": "3",
                "padding_top": 60,
                "padding_bottom": 60,
            },
        },
        "faq": {
            "type": "product-faq",
            "settings": {
                "heading": "Got Questions?",
                "subheading": "Find answers below or contact our support team.",
                "background_color": "#ffffff",
                "text_color": "#1d1d1d",
                "padding_top": 40,
                "padding_bottom": 60,
            },
        },
        "highlights": {
            "type": "dynamic-highlights-banner",
            "blocks": {
                "h1": {
                    "type": "highlight",
                    "settings": {
                        "icon": "icon-award-winning",
                        "title": "Authorized Dealer",
                        "text": "<p>Official products from trusted brands</p>",
                    },
                },
                "h2": {
                    "type": "highlight",
                    "settings": {
                        "icon": "icon-delivery-cart",
                        "title": "Free Shipping",
                        "text": "<p>On all orders across the US</p>",
                    },
                },
                "h3": {
                    "type": "highlight",
                    "settings": {
                        "icon": "icon-chat",
                        "title": "Expert Support",
                        "text": "<p>Technical help when you need it</p>",
                    },
                },
                "h4": {
                    "type": "highlight",
                    "settings": {
                        "icon": "icon-shield",
                        "title": "Secure Payments",
                        "text": "<p>Encrypted checkout you can trust</p>",
                    },
                },
            },
            "block_order": ["h1", "h2", "h3", "h4"],
            "settings": {
                "section_spacing": True,
                "section_width": "full-width",
                "icon_layout": "center",
                "color": "#1d1d1d",
                "icon_color": "#046e82",
                "background_color": "#ffffff",
                "mobile_layout": "grid",
            },
        },
        "recommendations": {
            "type": "static-product-recommendations",
            "settings": {
                "show_product_recommendations": True,
                "product_recommendations_heading": "You May Also Like",
            },
        },
    },
    "order": [
        "main",
        "image_with_text",
        "features",
        "faq",
        "highlights",
        "recommendations",
    ],
}
push_asset("templates/product.json", json.dumps(product))
time.sleep(0.5)

# --- 2. Header group ---
print("\n2. Pushing header-group.json...")
header = {
    "type": "header",
    "name": "Header",
    "sections": {
        "announcement-bar": {
            "type": "static-announcement",
            "settings": {
                "show_announcement": True,
                "homepage_announcement": False,
                "announcement_text": "Authorized Dealer \u2014 Free Shipping on All Orders",
                "announcement_text_mobile": "Authorized Dealer \u2014 Free Shipping",
                "announcement_color": "#ffffff",
                "announcement_background": "#1d1d1d",
            },
        },
        "header": {
            "type": "static-header",
            "settings": {
                "sticky_header": True,
                "full_width_header": True,
                "logo_height": 40,
                "logo_width": 180,
                "filter_search_by": "product_type",
                "enable_live_search": True,
                "show_mobile_search_bar": False,
                "enable_live_search_images": True,
                "quick_links": "",
                "menu": "main-menu",
                "secondary_menu": "",
                "small_promo_heading": "Expert Support",
                "small_promo_text": "<p>Monday to Friday, 9AM to 5PM (EST)</p>",
                "small_promo_text_mobile": "<p>Mon-Fri, 9AM-5PM EST</p>",
                "small_promo_icon": "icon-chat",
                "cart_icon": "icon-cart",
            },
        },
    },
    "order": ["announcement-bar", "header"],
}
push_asset("sections/header-group.json", json.dumps(header))
time.sleep(0.5)

# --- 3. Footer group ---
print("\n3. Pushing footer-group.json...")
footer = {
    "type": "footer",
    "name": "Footer",
    "sections": {
        "footer": {
            "type": "static-footer",
            "blocks": {
                "social_contact": {"type": "social_accounts", "settings": {}},
                "policies_menu": {
                    "type": "menu",
                    "settings": {"menu": "policies"},
                },
                "info_menu": {"type": "menu", "settings": {"menu": "info"}},
                "newsletter_block": {
                    "type": "newsletter",
                    "settings": {
                        "title": "Stay Updated",
                        "text": "<p>Your authorized source for surveying equipment and metal detectors. We partner directly with leading brands to bring you genuine products backed by full manufacturer support.</p>",
                    },
                },
            },
            "block_order": [
                "social_contact",
                "policies_menu",
                "info_menu",
                "newsletter_block",
            ],
            "settings": {
                "payment_icons": True,
                "show_locale_selector": False,
                "show_currency_selector": False,
                "additional_menu": "",
            },
        },
    },
    "order": ["footer"],
}
push_asset("sections/footer-group.json", json.dumps(footer))

print("\nAll templates pushed!")
