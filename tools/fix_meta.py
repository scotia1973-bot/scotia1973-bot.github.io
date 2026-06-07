#!/usr/bin/env python3
"""Fix OG titles/descriptions that still reference QR Code"""

import os

BASE = "/Users/scottwishart/scotia1973-bot.github.io"

TOOLS = [
    ("password-api", "Password Generator API", "Generate secure random passwords via REST API. Configurable length, symbols, numbers, uppercase. Free tier, no signup.",
     "Free Password Generator API. Generate cryptographically secure random passwords with configurable length, symbols, numbers, and uppercase letters. REST API, no key needed."),
    
    ("uuid", "UUID Generator API", "Generate UUID v4 identifiers via REST API. Single or batch. Free tier, no signup.",
     "Free UUID Generator API. Generate UUID v4 (random) identifiers via REST. Single or batch generation up to 1000 UUIDs. No API key required."),
    
    ("hash-api", "Hash Generator API", "Generate cryptographic hashes via REST API. Supports MD5, SHA-1, SHA-256, SHA-512. Free tier, no signup.",
     "Free Hash Generator API. Generate MD5, SHA-1, SHA-256, and SHA-512 hashes from any text. REST API for password hashing, data integrity, and digital signatures."),
    
    ("base64", "Base64 Encode/Decode API", "Encode and decode Base64 via simple REST API. Free tier, no signup. Perfect for developers needing Base64 transformations.",
     "Free Base64 Encode/Decode API. Encode or decode text using Base64 via REST. Perfect for data transport, API development, and debugging. No API key needed."),
    
    ("json-api", "JSON Prettify & Validate API", "Prettify, validate, and minify JSON via REST API. Free tier, no signup. Perfect for developers needing JSON processing.",
     "Free JSON Prettify and Validate API. Prettify, minify, or validate JSON strings via REST. Perfect for API debugging, configuration formatting, and data processing."),
    
    ("color", "Color Converter API", "Convert colors between HEX and RGB formats via REST API. Free tier, no signup.",
     "Free Color Converter API. Convert colors between HEX and RGB formats instantly via REST. Perfect for CSS, design systems, and web development."),
    
    ("email-verify", "Email Verification API", "Verify email addresses via REST API. Syntax check, domain verification, disposable email detection. Free tier, no signup.",
     "Free Email Verification API. Validate email addresses with syntax check, domain verification, and disposable email detection. REST API, no API key needed."),
    
    ("ip-geolocation", "IP Geolocation API", "Look up geolocation data for any IP address. Country, city, ISP, timezone. Free tier, no signup.",
     "Free IP Geolocation API. Look up IP address locations including country, city, ISP, and timezone. REST API, no API key needed."),
    
    ("timestamp", "Timestamp Converter API", "Convert Unix timestamps to dates and back via REST API. ISO 8601, RFC 2822 formats. Free tier, no signup.",
     "Free Timestamp Converter API. Convert Unix timestamps to human-readable dates and back. REST API supporting ISO 8601, RFC 2822, and custom formats."),
    
    ("lorem-ipsum", "Lorem Ipsum Generator API", "Generate Lorem Ipsum placeholder text via REST API. Paragraphs, sentences, or words. Free tier, no signup.",
     "Free Lorem Ipsum Generator API. Generate placeholder text in paragraphs, sentences, or words via REST. Perfect for mockups, wireframes, and design drafts."),
    
    ("currency", "Currency Converter API", "Convert between 150+ currencies with real-time exchange rates via REST API. Free tier, no signup.",
     "Free Currency Converter API. Convert between 150+ world currencies with real-time exchange rates. REST API for developers building finance apps."),
    
    ("weather", "Weather API", "Get current weather conditions and forecasts for any city via REST API. Free tier, no signup.",
     "Free Weather API. Get current weather conditions, temperature, humidity, and forecasts for any city. REST API for developers."),
    
    ("geocoding", "Geocoding API", "Convert addresses to coordinates and back via REST API. Free tier, no signup.",
     "Free Geocoding API. Convert addresses to geographic coordinates (latitude/longitude) and reverse geocode coordinates to addresses."),
    
    ("random-password", "Random Data Generator API", "Generate random passwords, numbers, strings, and tokens via REST API. Free tier, no signup.",
     "Free Random Data Generator API. Generate random passwords, numbers, tokens, strings, and more via REST API."),
    
    ("unit-converter", "Unit Converter API", "Convert between hundreds of measurement units via REST API. Free tier, no signup.",
     "Free Unit Converter API. Convert between length, weight, temperature, volume, area, speed, and more measurement units via REST."),
    
    ("roman-numerals", "Roman Numeral Converter API", "Convert numbers to Roman numerals and back via REST API. Free tier, no signup.",
     "Free Roman Numeral Converter API. Convert numbers to Roman numerals and parse Roman numerals back to numbers via REST API."),
    
    ("case-converter", "Text Case Converter API", "Convert text between uppercase, lowercase, title case, camelCase and more via REST API. Free tier.",
     "Free Text Case Converter API. Convert text to uppercase, lowercase, title case, sentence case, camelCase, snake_case and more via REST."),
    
    ("morse-code", "Morse Code Converter API", "Convert text to Morse code and decode Morse back to text via REST API. Free tier, no signup.",
     "Free Morse Code Converter API. Convert text to Morse code and decode Morse code back to text via REST API for developers."),
    
    ("nato-phonetic", "NATO Phonetic Alphabet API", "Convert text to NATO phonetic alphabet words for clear voice communication via REST API. Free tier.",
     "Free NATO Phonetic Alphabet API. Convert text to NATO phonetic alphabet words (Alpha, Bravo, Charlie) for clear radio communication."),
]

for slug, name, og_desc, meta_desc in TOOLS:
    filepath = os.path.join(BASE, "tools", slug, "index.html")
    if not os.path.exists(filepath):
        print("SKIP " + slug + " - no file")
        continue
    
    with open(filepath, "r") as f:
        page = f.read()
    
    # Fix OG title
    page = page.replace(
        '<meta property="og:title" content="QR Code Generator API — Free QR Code REST API">',
        '<meta property="og:title" content="' + name + ' — ' + og_desc + '">'
    )
    
    # Fix OG title without " — " 
    page = page.replace(
        "QR Code Generator API — Free QR Code REST API",
        name + " — " + og_desc
    )
    
    # Fix meta description (still has QR code text)
    old_desc = "Free QR Code Generator API. Generate QR codes from URLs, text, or any data. REST API with PNG, SVG support. No API key needed for free tier. 100 requests/day free."
    page = page.replace(old_desc, meta_desc)
    
    # Fix OG description
    old_og_desc = "Generate QR codes from any text or URL. Free REST API, no signup needed. PNG, SVG, GIF output. Custom colors and sizes."
    page = page.replace(old_og_desc, og_desc)
    
    with open(filepath, "w") as f:
        f.write(page)
    print("Fixed " + slug)

print("Done!")
