#!/usr/bin/env python3
"""Fix remaining QR Code references in generated pages"""

import os, re

BASE = "/Users/scottwishart/scotia1973-bot.github.io"

TOOLS = [
    ("password-api", "Password Generator API", "🔑", "/password"),
    ("uuid", "UUID Generator API", "🎲", "/uuid"),
    ("hash-api", "Hash Generator API", "📁", "/hash"),
    ("base64", "Base64 Encode/Decode API", "🔤", "/base64"),
    ("json-api", "JSON Prettify & Validate API", "📋", "/json"),
    ("color", "Color Converter API", "🎨", "/color"),
    ("email-verify", "Email Verification API", "✉️", "/email-verify"),
    ("ip-geolocation", "IP Geolocation API", "🌍", "/ip"),
    ("timestamp", "Timestamp Converter API", "⏰", "/timestamp"),
    ("lorem-ipsum", "Lorem Ipsum Generator API", "📝", "/lorem"),
    ("currency", "Currency Converter API", "💰", "/currency"),
    ("weather", "Weather API", "🌤️", "/weather"),
    ("geocoding", "Geocoding API", "🗺️", "/geocoding"),
    ("random-password", "Random Data Generator API", "🎲", "/random-password"),
    ("unit-converter", "Unit Converter API", "📐", "/unit-converter"),
    ("roman-numerals", "Roman Numeral Converter API", "🏛️", "/roman-numerals"),
    ("case-converter", "Text Case Converter API", "🔤", "/case-converter"),
    ("morse-code", "Morse Code Converter API", "📡", "/morse-code"),
    ("nato-phonetic", "NATO Phonetic Alphabet API", "🔊", "/nato-phonetic"),
]

for slug, name, emoji, endpoint_path in TOOLS:
    filepath = os.path.join(BASE, "tools", slug, "index.html")
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, "r") as f:
        page = f.read()
    
    replacements = [
        ("QR code/", name + "/"),
        ("QR code?", name + "?"),
        ("QR code", name),
        ("qr code", name),
        ("QR Code", name),
        ("qr-code", slug),
        ("qr code", slug),
        ("qrcode", slug),
        # Fix emoji
        ("📱", emoji),
        # Fix endpoint references
        ("/qr?", endpoint_path + "?"),
        ("/qr/", endpoint_path + "/"),
        ("/qr", endpoint_path),
        ("api.gadgethumans.com/qr?", "api.gadgethumans.com" + endpoint_path + "?"),
        ("api.gadgethumans.com/qr/", "api.gadgethumans.com" + endpoint_path + "/"),
        ("api.gadgethumans.com/qr\n", "api.gadgethumans.com" + endpoint_path + "\n"),
        ("api.gadgethumans.com/qr", "api.gadgethumans.com" + endpoint_path),
        # QR Code API Docs → API Docs
        ("QR Code API Docs", name + " API Docs"),
        # Generate QR Code → Call API
        ("Generate QR Code", "Call API"),
        ("generateQR()", "callAPI()"),
    ]
    
    for old, new in replacements:
        page = page.replace(old, new)
    
    # Also clean up any double-replaced names
    page = page.replace(name + name, name)
    
    with open(filepath, "w") as f:
        f.write(page)
    
    # Count remaining
    remaining = page.lower().count("qr") + page.lower().count("qrcode")
    print(f"{slug}: {remaining} QR refs remaining")

print("Done!")
