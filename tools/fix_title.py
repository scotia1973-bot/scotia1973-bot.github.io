#!/usr/bin/env python3
"""Fix remaining title and og:title that still reference QR Code"""

import os

BASE = "/Users/scottwishart/scotia1973-bot.github.io"

TOOLS = [
    ("password-api", "Password Generator API", "Free Secure Password API | GadgetHumans", "Free Secure Password REST API"),
    ("uuid", "UUID Generator API", "Free UUID v4 REST API | GadgetHumans", "Free UUID v4 REST API"),
    ("hash-api", "Hash Generator API", "Free Cryptographic Hash REST API | GadgetHumans", "Free Cryptographic Hash REST API"),
    ("base64", "Base64 Encode/Decode API", "Free Base64 REST API | GadgetHumans", "Free Base64 REST API"),
    ("json-api", "JSON Prettify API", "Free JSON Format & Validate REST API | GadgetHumans", "Free JSON Format & Validate REST API"),
    ("color", "Color Converter API", "Free HEX to RGB Converter REST API | GadgetHumans", "Free HEX to RGB Converter REST API"),
    ("email-verify", "Email Verification API", "Free Email Validator REST API | GadgetHumans", "Free Email Validator REST API"),
    ("ip-geolocation", "IP Geolocation API", "Free IP Location REST API | GadgetHumans", "Free IP Location REST API"),
    ("timestamp", "Timestamp Converter API", "Free Unix Timestamp Converter REST API | GadgetHumans", "Free Unix Timestamp Converter REST API"),
    ("lorem-ipsum", "Lorem Ipsum Generator API", "Free Placeholder Text REST API | GadgetHumans", "Free Placeholder Text REST API"),
    ("currency", "Currency Converter API", "Free Exchange Rate REST API | GadgetHumans", "Free Exchange Rate REST API"),
    ("weather", "Weather API", "Free Weather Data REST API | GadgetHumans", "Free Weather Data REST API"),
    ("geocoding", "Geocoding API", "Free Address to Coordinates REST API | GadgetHumans", "Free Address to Coordinates REST API"),
    ("random-password", "Random Data Generator API", "Free Random Data REST API | GadgetHumans", "Free Random Data REST API"),
    ("unit-converter", "Unit Converter API", "Free Measurement Conversion REST API | GadgetHumans", "Free Measurement Conversion REST API"),
    ("roman-numerals", "Roman Numeral Converter API", "Free Roman Numerals REST API | GadgetHumans", "Free Roman Numerals REST API"),
    ("case-converter", "Text Case Converter API", "Free String Case REST API | GadgetHumans", "Free String Case REST API"),
    ("morse-code", "Morse Code Converter API", "Free Text to Morse REST API | GadgetHumans", "Free Text to Morse REST API"),
    ("nato-phonetic", "NATO Phonetic Alphabet API", "Free Phonetic Converter REST API | GadgetHumans", "Free Phonetic Converter REST API"),
]

for slug, name, title_suffix, og_suffix in TOOLS:
    filepath = os.path.join(BASE, "tools", slug, "index.html")
    if not os.path.exists(filepath):
        print("SKIP " + slug)
        continue
    
    with open(filepath, "r") as f:
        page = f.read()
    
    # Fix <title> tag
    # Old pattern: <title>NAME — Free QR Code API | GadgetHumans</title>
    old_title = '<title>' + name + ' \u2014 Free QR Code API | GadgetHumans</title>'
    new_title = '<title>' + name + ' \u2014 ' + title_suffix + '</title>'
    page = page.replace(old_title, new_title)
    
    # Fix og:title
    # Old pattern: <meta property="og:title" content="NAME — Free QR Code REST API">
    old_og = '<meta property="og:title" content="' + name + ' \u2014 Free QR Code REST API">'
    new_og = '<meta property="og:title" content="' + name + ' \u2014 ' + og_suffix + '">'
    page = page.replace(old_og, new_og)
    
    # Fix any remaining "Free QR Code" references in the hero description
    page = page.replace("Free QR Code REST API", og_suffix)
    
    with open(filepath, "w") as f:
        f.write(page)
    print("Fixed " + slug)

print("Done!")
