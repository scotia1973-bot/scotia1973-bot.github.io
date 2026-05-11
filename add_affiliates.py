#!/usr/bin/env python3
"""Inject Amazon affiliate "Pro Tip" sections into all tool pages on gadgethumans.com."""

import os
import re

TOOLS_DIR = os.path.expanduser("~/Desktop/scotia1973-bot.github.io/tools")
AMAZON_TAG = "gadgethumans-21"

# Product-to-tool mapping with Amazon ASINs
# Format: (filename_pattern, amazon_link_text, amazon_asins, emoji)
# Each tool gets varied products from its category

TOOL_MAP = {
    # ── Security / Password tools → YubiKey ──
    "password": {
        "tips": [
            ("YubiKey 5C NFC", "B0BGNN1BB9", "🔐"),
            ("YubiKey 5 Series", "B0BGNN1BB9", "🔐"),
        ]
    },
    "secure-password": {
        "tips": [
            ("YubiKey 5C NFC", "B0BGNN1BB9", "🔐"),
            ("YubiKey USB-A + Lightning", "B0BGNN1BB9", "🔐"),
        ]
    },
    "password-strength": {
        "tips": [
            ("YubiKey 5C NFC", "B0BGNN1BB9", "🔐"),
            ("YubiKey 5 NFC", "B0BGNN1BB9", "🔐"),
        ]
    },
    "pin-generator": {
        "tips": [
            ("YubiKey 5C NFC", "B0BGNN1BB9", "🔐"),
            ("YubiKey 5 Series", "B0BGNN1BB9", "🔐"),
        ]
    },
    # ── Hash / Encryption tools → YubiKey ──
    "hash": {
        "tips": [
            ("YubiKey 5C NFC", "B0BGNN1BB9", "🔐"),
        ]
    },
    "md5-generator": {
        "tips": [
            ("YubiKey 5C NFC", "B0BGNN1BB9", "🔐"),
        ]
    },
    "sha256-generator": {
        "tips": [
            ("YubiKey 5C NFC", "B0BGNN1BB9", "🔐"),
        ]
    },
    "sha512-generator": {
        "tips": [
            ("YubiKey 5C NFC", "B0BGNN1BB9", "🔐"),
        ]
    },
    # ── Text / Code tools → Keychron mechanical keyboards ──
    "lorem": {
        "tips": [
            ("Keychron Q1 Pro Keyboard", "B0C2DX2JLY", "⌨️"),
        ]
    },
    "json-formatter": {
        "tips": [
            ("Keychron Q1 Pro Mechanical Keyboard", "B0C2DX2JLY", "⌨️"),
        ]
    },
    "lowercase-converter": {
        "tips": [
            ("Keychron K2 Pro Keyboard", "B0BLBZDG6C", "⌨️"),
        ]
    },
    "uppercase-converter": {
        "tips": [
            ("Keychron K2 Pro Keyboard", "B0BLBZDG6C", "⌨️"),
        ]
    },
    "sentence-case-converter": {
        "tips": [
            ("Keychron Q1 Pro Keyboard", "B0C2DX2JLY", "⌨️"),
        ]
    },
    "title-case-converter": {
        "tips": [
            ("Keychron Q1 Pro", "B0C2DX2JLY", "⌨️"),
        ]
    },
    "textcase": {
        "tips": [
            ("Keychron K2 Pro", "B0BLBZDG6C", "⌨️"),
        ]
    },
    "character-counter": {
        "tips": [
            ("Keychron Q1 Pro Keyboard", "B0C2DX2JLY", "⌨️"),
        ]
    },
    "word-counter": {
        "tips": [
            ("Keychron K2 Pro Keyboard", "B0BLBZDG6C", "⌨️"),
        ]
    },
    "wordcount": {
        "tips": [
            ("Keychron K2 Pro", "B0BLBZDG6C", "⌨️"),
        ]
    },
    "sentence-counter": {
        "tips": [
            ("Keychron Q1 Pro", "B0C2DX2JLY", "⌨️"),
        ]
    },
    "tts-character-counter": {
        "tips": [
            ("Keychron K2 Pro", "B0BLBZDG6C", "⌨️"),
        ]
    },
    "reading-time-calculator": {
        "tips": [
            ("Keychron Q1 Pro", "B0C2DX2JLY", "⌨️"),
        ]
    },
    # ── URL / Encoding tools → Keychron ──
    "url-encoder": {
        "tips": [
            ("Keychron K2 Pro", "B0BLBZDG6C", "⌨️"),
        ]
    },
    "url-decoder": {
        "tips": [
            ("Keychron K2 Pro", "B0BLBZDG6C", "⌨️"),
        ]
    },
    "urlencode": {
        "tips": [
            ("Keychron K2 Pro", "B0BLBZDG6C", "⌨️"),
        ]
    },
    "base64-encoder": {
        "tips": [
            ("Keychron Q1 Pro", "B0C2DX2JLY", "⌨️"),
        ]
    },
    "base64-decoder": {
        "tips": [
            ("Keychron Q1 Pro", "B0C2DX2JLY", "⌨️"),
        ]
    },
    # ── Color tools → Color-calibrated monitors ──
    "colorpicker": {
        "tips": [
            ("Dell S2722QC 4K Monitor", "B09V3MQKC8", "🖥️"),
        ]
    },
    "color-contrast-checker": {
        "tips": [
            ("Dell S2722QC 4K USB-C Monitor", "B09V3MQKC8", "🖥️"),
        ]
    },
    "hex-to-rgb": {
        "tips": [
            ("BenQ PD2705U 4K Monitor", "B08VMX4L2G", "🖥️"),
        ]
    },
    "rgb-to-hex": {
        "tips": [
            ("Dell S2722QC 4K Monitor", "B09V3MQKC8", "🖥️"),
        ]
    },
    "hex-to-decimal": {
        "tips": [
            ("Dell S2722QC 4K Monitor", "B09V3MQKC8", "🖥️"),
        ]
    },
    "hex": {
        "tips": [
            ("Dell UltraSharp 27\" 4K", "B09V3MQKC8", "🖥️"),
        ]
    },
    # ── Calculator / Converter tools → Drawing tablets ──
    "bmi-calculator": {
        "tips": [
            ("Wacom Intuos Small Drawing Tablet", "B079GMGR4N", "✏️"),
        ]
    },
    "bmi": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "ideal-weight-calculator": {
        "tips": [
            ("Wacom Intuos Drawing Tablet", "B079GMGR4N", "✏️"),
        ]
    },
    "calorie": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "percentage": {
        "tips": [
            ("Wacom Intuos Drawing Tablet", "B079GMGR4N", "✏️"),
        ]
    },
    "percentage-change-calculator": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "percentage-decrease-calculator": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "percentage-increase-calculator": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "percentage-of-number": {
        "tips": [
            ("Wacom Intuos Small Drawing Tablet", "B079GMGR4N", "✏️"),
        ]
    },
    "fraction-to-percentage": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "tip-calculator": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "tip": {
        "tips": [
            ("Wacom Intuos Drawing Tablet", "B079GMGR4N", "✏️"),
        ]
    },
    "restaurant-tip-calculator": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "bill-splitter": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "loan": {
        "tips": [
            ("Wacom Intuos Drawing Tablet", "B079GMGR4N", "✏️"),
        ]
    },
    "loan-payment-calculator": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "car-loan-calculator": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "mortgage-calculator": {
        "tips": [
            ("Wacom Intuos Drawing Tablet", "B079GMGR4N", "✏️"),
        ]
    },
    "mortgage-payment-calculator": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "mortgage-affordability": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "personal-loan-calculator": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "rent-vs-buy-calculator": {
        "tips": [
            ("Wacom Intuos Small Drawing Tablet", "B079GMGR4N", "✏️"),
        ]
    },
    "ai-cost-calculator": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "age": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "birthday": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "dates": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "days-between-dates": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "weeks-between-dates": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "business-days-calculator": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "random": {
        "tips": [
            ("Wacom Intuos Drawing Tablet", "B079GMGR4N", "✏️"),
        ]
    },
    "random-number-generator": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "random-team-generator": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "lottery-number-generator": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "coin-flip": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "dice-roller": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "screen-resolution": {
        "tips": [
            ("Dell S2722QC 4K Monitor", "B09V3MQKC8", "🖥️"),
        ]
    },
    "meeting-time-planner": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "timezone-converter": {
        "tips": [
            ("Dell S2722QC 4K Monitor", "B09V3MQKC8", "🖥️"),
        ]
    },
    "timezone": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "utc-converter": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "world-clock": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    # ── Conversion tools → Drawing tablets ──
    "binary-to-decimal": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "decimal-to-binary": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "decimal-to-hex": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "celsius-to-fahrenheit": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "fahrenheit-to-celsius": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "cm-to-inches": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "inches-to-cm": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "feet-to-meters": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "meters-to-feet": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "kg-to-lbs": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "lbs-to-kg": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "convert-area": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "convert-length": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "convert-pressure": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "convert-speed": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "convert-temperature": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "convert-volume": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "convert-weight": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    "converter": {
        "tips": [
            ("Wacom Intuos Small", "B079GMGR4N", "✏️"),
        ]
    },
    # ── Timer / Stopwatch → Smart speaker ──
    "stopwatch": {
        "tips": [
            ("Echo Dot (5th Gen)", "B09B8W5FW7", "⏰"),
        ]
    },
    "countdown": {
        "tips": [
            ("Echo Dot (5th Gen)", "B09B8W5FW7", "⏰"),
        ]
    },
    "timer": {
        "tips": [
            ("Echo Dot (5th Gen)", "B09B8W5FW7", "⏰"),
        ]
    },
}


def find_mapping(filename):
    """Find the best mapping for a given filename."""
    fname = filename.replace(".html", "")
    
    # Try exact match first
    if fname in TOOL_MAP:
        return TOOL_MAP[fname]
    
    # Try prefix match
    for key in TOOL_MAP:
        if fname.startswith(key):
            return TOOL_MAP[key]
    
    return None


def build_pro_tip_section(product_name, asin, emoji):
    """Build the Pro Tip section HTML."""
    return f"""  <!-- Pro Tip -->
  <div class="card" style="max-width: 700px; margin: 32px auto; padding: 20px 24px; background: var(--glass-bg); backdrop-filter: blur(var(--glass-blur-sm)); -webkit-backdrop-filter: blur(var(--glass-blur-sm)); border: 1px solid var(--glass-border); border-radius: var(--radius-lg);">
    <div style="display: flex; align-items: flex-start; gap: 12px;">
      <div style="font-size: 1.5rem; line-height: 1;">💡</div>
      <div style="flex: 1;">
        <p style="margin: 0 0 6px; font-size: 0.85rem; font-weight: 700; color: var(--text);">Pro Tip</p>
        <p style="margin: 0; font-size: 0.8rem; color: var(--text2); line-height: 1.5;">
          Love free tools? Level up your workspace with the
          <a href="https://www.amazon.com/dp/{asin}?tag={AMAZON_TAG}" target="_blank" rel="nofollow sponsored" style="color: var(--accent); text-decoration: underline; font-weight: 600;">{emoji} {product_name}</a>
          — a favorite among pros on Amazon.
        </p>
      </div>
    </div>
  </div>
"""


def process_file(filepath):
    """Inject Pro Tip section into a tool HTML file."""
    filename = os.path.basename(filepath)
    
    # Skip index, redirects
    if filename == "index.html" or filename == "countdown.html" or filename == "timer.html":
        return None
    
    mapping = find_mapping(filename)
    if not mapping:
        return f"NO MAPPING: {filename}"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use first tip from the mapping
    tip = mapping["tips"][0]
    product_name, asin, emoji = tip
    
    pro_tip_html = build_pro_tip_section(product_name, asin, emoji)
    
    # Insert before the <div class="promo"> section
    target = '\n  <div class="promo">'
    
    if target in content:
        new_content = content.replace(target, f'\n{pro_tip_html}{target}', 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return f"✓ {filename} → {emoji} {product_name}"
    else:
        return f"NO PROMO TAG: {filename}"


def main():
    results = []
    success = 0
    skipped = 0
    errors = 0
    
    for fname in sorted(os.listdir(TOOLS_DIR)):
        if not fname.endswith(".html"):
            continue
        
        filepath = os.path.join(TOOLS_DIR, fname)
        result = process_file(filepath)
        
        if result is None:
            skipped += 1
        elif result.startswith("✓"):
            success += 1
            results.append(result)
        else:
            errors += 1
            results.append(result)
    
    print(f"\n{'='*60}")
    print(f"Done! Success: {success}, Skipped: {skipped}, Errors: {errors}")
    print(f"{'='*60}")
    for r in results:
        print(r)


if __name__ == "__main__":
    main()
