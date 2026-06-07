#!/usr/bin/env python3
"""Generate all 20 API tool landing pages from QR code template"""

import os

BASE = "/Users/scottwishart/scotia1973-bot.github.io"

# Read the QR code base template
with open(os.path.join(BASE, "tools/qr-code/index.html"), "r") as f:
    QR_PAGE = f.read()

# All tools data
TOOLS = [
    ("password-api", "🔑", "Password Generator API",
     "Password Generator API — Free Secure Password API | GadgetHumans",
     "Free Password Generator API. Generate cryptographically secure random passwords with configurable length, symbols, numbers, and uppercase letters. REST API, no key needed.",
     "password generator API, secure password API, random password generator REST API, free password API, developer password tool",
     "Generate secure random passwords via REST API. Configurable length, symbols, numbers, uppercase. Free tier, no signup.",
     "/password",
     "GET https://api.gadgethumans.com/password?length=16&symbols=true&numbers=true&uppercase=true"),

    ("uuid", "🎲", "UUID Generator API",
     "UUID Generator API — Free UUID v4 REST API | GadgetHumans",
     "Free UUID Generator API. Generate UUID v4 (random) identifiers via REST. Single or batch generation up to 1000 UUIDs. No API key required.",
     "UUID generator API, UUID v4 API, random UUID API, free UUID API, generate UUID REST API, unique identifier API",
     "Generate UUID v4 identifiers via REST API. Single or batch. Free tier, no signup.",
     "/uuid",
     "GET https://api.gadgethumans.com/uuid?count=1&format=standard"),

    ("hash-api", "📁", "Hash Generator API",
     "Hash Generator API — Free Cryptographic Hash REST API | GadgetHumans",
     "Free Hash Generator API. Generate MD5, SHA-1, SHA-256, and SHA-512 hashes from any text. REST API for password hashing, data integrity, and digital signatures.",
     "hash generator API, SHA-256 API, MD5 API, SHA-512 API, cryptographic hash API, free hashing API, REST hash endpoint",
     "Generate cryptographic hashes via REST API. Supports MD5, SHA-1, SHA-256, SHA-512. Free tier, no signup.",
     "/hash",
     "GET https://api.gadgethumans.com/hash?text=hello&algorithm=sha256"),

    ("base64", "🔤", "Base64 Encode/Decode API",
     "Base64 Encode/Decode API — Free Base64 REST API | GadgetHumans",
     "Free Base64 Encode/Decode API. Encode or decode text using Base64 via REST. Perfect for data transport, API development, and debugging. No API key needed.",
     "Base64 API, Base64 encode API, Base64 decode API, free Base64 encoder, Base64 REST endpoint, data encoding API",
     "Encode and decode Base64 via simple REST API. Free tier, no signup. Perfect for developers needing Base64 transformations.",
     "/base64",
     "GET https://api.gadgethumans.com/base64?text=hello&mode=encode"),

    ("json-api", "📋", "JSON Prettify & Validate API",
     "JSON Prettify API — Free JSON Format & Validate REST API | GadgetHumans",
     "Free JSON Prettify and Validate API. Prettify, minify, or validate JSON strings via REST. Perfect for API debugging, configuration formatting, and data processing.",
     "JSON prettify API, JSON validate API, JSON minify API, JSON formatter REST API, free JSON API, JSON beautifier",
     "Prettify, validate, and minify JSON via REST API. Free tier, no signup. Perfect for developers needing JSON processing.",
     "/json",
     "GET https://api.gadgethumans.com/json?json={\"k\":\"v\"}&mode=prettify"),

    ("color", "🎨", "Color Converter API",
     "Color Converter API — Free HEX to RGB Converter REST API | GadgetHumans",
     "Free Color Converter API. Convert colors between HEX and RGB formats instantly via REST. Perfect for CSS, design systems, and web development.",
     "color converter API, HEX to RGB API, RGB to HEX API, color conversion REST API, free color API, CSS color converter",
     "Convert colors between HEX and RGB formats via REST API. Free tier, no signup.",
     "/color",
     "GET https://api.gadgethumans.com/color?value=FF0000&from=hex&to=rgb"),

    ("email-verify", "✉️", "Email Verification API",
     "Email Verification API — Free Email Validator REST API | GadgetHumans",
     "Free Email Verification API. Validate email addresses with syntax check, domain verification, and disposable email detection. REST API, no API key needed.",
     "email verification API, email validator API, free email check API, email validation REST API, disposable email detector",
     "Verify email addresses via REST API. Syntax check, domain verification, disposable email detection. Free tier, no signup.",
     "/email-verify",
     "GET https://api.gadgethumans.com/email-verify?email=user@example.com"),

    ("ip-geolocation", "🌍", "IP Geolocation API",
     "IP Geolocation API — Free IP Location REST API | GadgetHumans",
     "Free IP Geolocation API. Look up IP address locations including country, city, ISP, and timezone. REST API, no API key needed.",
     "IP geolocation API, IP lookup API, free IP location API, IP address geolocation, geo IP REST API",
     "Look up geolocation data for any IP address. Country, city, ISP, timezone. Free tier, no signup.",
     "/ip",
     "GET https://api.gadgethumans.com/ip?ip_address=8.8.8.8"),

    ("timestamp", "⏰", "Timestamp Converter API",
     "Timestamp Converter API — Free Unix Timestamp Converter REST API | GadgetHumans",
     "Free Timestamp Converter API. Convert Unix timestamps to human-readable dates and back. REST API supporting ISO 8601, RFC 2822, and custom formats.",
     "timestamp converter API, Unix timestamp API, epoch converter API, date converter REST API, free timestamp tool",
     "Convert Unix timestamps to dates and back via REST API. ISO 8601, RFC 2822 formats. Free tier, no signup.",
     "/timestamp",
     "GET https://api.gadgethumans.com/timestamp?value=1717000000&format=iso"),

    ("lorem-ipsum", "📝", "Lorem Ipsum Generator API",
     "Lorem Ipsum Generator API — Free Placeholder Text REST API | GadgetHumans",
     "Free Lorem Ipsum Generator API. Generate placeholder text in paragraphs, sentences, or words via REST. Perfect for mockups, wireframes, and design drafts.",
     "lorem ipsum API, placeholder text generator API, lorem ipsum generator REST API, free lorem ipsum tool, dummy text API",
     "Generate Lorem Ipsum placeholder text via REST API. Paragraphs, sentences, or words. Free tier, no signup.",
     "/lorem",
     "GET https://api.gadgethumans.com/lorem?type=paragraphs&count=3"),

    ("currency", "💰", "Currency Converter API",
     "Currency Converter API — Free Exchange Rate REST API | GadgetHumans",
     "Free Currency Converter API. Convert between 150+ world currencies with real-time exchange rates. REST API for developers building finance apps.",
     "currency converter API, exchange rate API, free currency API, forex API, currency conversion REST API",
     "Convert between 150+ currencies with real-time exchange rates via REST API. Free tier, no signup.",
     "/currency",
     "GET https://api.gadgethumans.com/currency?from=USD&to=EUR&amount=100"),

    ("weather", "🌤️", "Weather API",
     "Weather API — Free Weather Data REST API | GadgetHumans",
     "Free Weather API. Get current weather conditions, temperature, humidity, and forecasts for any city. REST API for developers. No API key needed.",
     "weather API, free weather API, weather data API, current weather REST API, weather forecast API",
     "Get current weather conditions and forecasts for any city via REST API. Free tier, no signup.",
     "/weather",
     "GET https://api.gadgethumans.com/weather?city=London&units=metric"),

    ("geocoding", "🗺️", "Geocoding API",
     "Geocoding API — Free Address to Coordinates REST API | GadgetHumans",
     "Free Geocoding API. Convert addresses to geographic coordinates (latitude/longitude) and reverse geocode coordinates to addresses.",
     "geocoding API, address to coordinates API, reverse geocoding API, free geocoding REST API, latitude longitude API",
     "Convert addresses to coordinates and back via REST API. Free tier, no signup.",
     "/geocoding",
     "GET https://api.gadgethumans.com/geocoding?address=1600+Amphitheatre+Parkway"),

    ("random-password", "🎲", "Random Data Generator API",
     "Random Data Generator API — Free Random Data REST API | GadgetHumans",
     "Free Random Data Generator API. Generate random passwords, numbers, tokens, strings, and more via REST API.",
     "random data generator API, random password API, random number API, random string API, free random data REST API",
     "Generate random passwords, numbers, strings, and tokens via REST API. Free tier, no signup.",
     "/random-password",
     "GET https://api.gadgethumans.com/random-password?length=16&type=password"),

    ("unit-converter", "📐", "Unit Converter API",
     "Unit Converter API — Free Measurement Conversion REST API | GadgetHumans",
     "Free Unit Converter API. Convert between length, weight, temperature, volume, area, speed, and more measurement units via REST.",
     "unit converter API, measurement conversion API, length converter API, weight converter API, temperature converter API",
     "Convert between hundreds of measurement units via REST API. Free tier, no signup.",
     "/unit-converter",
     "GET https://api.gadgethumans.com/unit-converter?value=100&from=kg&to=lbs"),

    ("roman-numerals", "🏛️", "Roman Numeral Converter API",
     "Roman Numeral Converter API — Free Roman Numerals REST API | GadgetHumans",
     "Free Roman Numeral Converter API. Convert numbers to Roman numerals and parse Roman numerals back to numbers via REST API.",
     "roman numeral converter API, number to roman API, roman to number API, free roman numeral REST API",
     "Convert numbers to Roman numerals and back via REST API. Free tier, no signup.",
     "/roman-numerals",
     "GET https://api.gadgethumans.com/roman-numerals?value=2024"),

    ("case-converter", "🔤", "Text Case Converter API",
     "Text Case Converter API — Free String Case REST API | GadgetHumans",
     "Free Text Case Converter API. Convert text to uppercase, lowercase, title case, sentence case, camelCase, snake_case and more via REST.",
     "case converter API, text case API, uppercase API, lowercase API, title case API, camel case API",
     "Convert text between uppercase, lowercase, title case, camelCase and more via REST API. Free tier.",
     "/case-converter",
     "GET https://api.gadgethumans.com/case-converter?text=hello+world&case=upper"),

    ("morse-code", "📡", "Morse Code Converter API",
     "Morse Code Converter API — Free Text to Morse REST API | GadgetHumans",
     "Free Morse Code Converter API. Convert text to Morse code and decode Morse code back to text via REST API for developers.",
     "morse code API, text to morse API, morse decoder API, free morse code converter REST API",
     "Convert text to Morse code and decode Morse back to text via REST API. Free tier, no signup.",
     "/morse-code",
     "GET https://api.gadgethumans.com/morse-code?text=SOS"),

    ("nato-phonetic", "🔊", "NATO Phonetic Alphabet API",
     "NATO Phonetic Alphabet API — Free Phonetic Converter REST API | GadgetHumans",
     "Free NATO Phonetic Alphabet API. Convert text to NATO phonetic alphabet words (Alpha, Bravo, Charlie) for clear radio communication.",
     "NATO phonetic alphabet API, phonetic converter API, Alpha Bravo Charlie API, ICAO phonetic API, spelling alphabet API",
     "Convert text to NATO phonetic alphabet words for clear voice communication via REST API. Free tier.",
     "/nato-phonetic",
     "GET https://api.gadgethumans.com/nato-phonetic?text=HELLO"),
]

for slug, emoji, name, title, meta_desc, meta_keywords, og_desc, endpoint_path, endpoint in TOOLS:
    page = QR_PAGE
    
    # -- General replacements --
    page = page.replace("QR Code Generator API", name)
    page = page.replace("📱", emoji)
    
    # URL paths
    page = page.replace("/tools/qr-code/", "/tools/" + slug + "/")
    page = page.replace("https://www.gadgethumans.com/tools/qr-code/", "https://www.gadgethumans.com/tools/" + slug + "/")
    page = page.replace("/qr?", endpoint_path + "?")
    page = page.replace("/qr", endpoint_path)  # must be after /qr? replacement
    
    # API URL base (for links)
    page = page.replace("api.gadgethumans.com/qr?", "api.gadgethumans.com" + endpoint_path + "?")
    page = page.replace("api.gadgethumans.com/qr", "api.gadgethumans.com" + endpoint_path)
    
    # -- Meta tags --
    page = page.replace("QR Code Generator API — Free QR Code API | GadgetHumans", title)
    page = page.replace(
        "Free QR Code Generator API. Generate QR codes from URLs, text, or any data. REST API with PNG, SVG support. No API key needed for free tier. 100 requests/day free.",
        meta_desc
    )
    page = page.replace(
        "QR code API, QR code generator API, free QR code API, QR code REST API, generate QR code, QR code PNG API, QR code SVG API, developer QR code",
        meta_keywords
    )
    
    # OG descriptions
    page = page.replace(
        "Generate QR codes from any text or URL. Free REST API, no signup needed. PNG, SVG, GIF output. Custom colors and sizes.",
        og_desc
    )
    page = page.replace(
        "Generate QR codes from any text or URL with a simple REST API call. Supports PNG, SVG, and GIF output. No API key required for the free tier.",
        og_desc
    )
    
    # Endpoint badge
    page = page.replace(
        "GET https://api.gadgethumans.com/qr?text=...&format=png|svg",
        endpoint
    )
    
    # JSON-LD name references
    page = page.replace('"QR Code Generator API"', '"' + name + '"')
    
    # API docs link
    page = page.replace(
        'href="https://api.gadgethumans.com/qr/',
        'href="https://api.gadgethumans.com' + endpoint_path + '/'
    )
    
    # -- Try It Live form --
    qr_form = """      <h3>Generate a QR Code</h3>
      <label for="qrText">Text or URL to encode</label>
      <input type="text" id="qrText" value="https://www.gadgethumans.com" placeholder="Enter text or URL...">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
        <div>
          <label for="qrFormat">Format</label>
          <select id="qrFormat">
            <option value="png">PNG</option>
            <option value="svg">SVG</option>
            <option value="gif">GIF</option>
          </select>
        </div>
        <div>
          <label for="qrSize">Size (px)</label>
          <select id="qrSize">
            <option value="200">200</option>
            <option value="300" selected>300</option>
            <option value="500">500</option>
            <option value="800">800</option>
          </select>
        </div>
      </div>
      <button class="btn" onclick="generateQR()">Generate QR Code \u2192</button>
      <div class="result" id="qrResult" style="text-align:center; display:flex; flex-direction:column; align-items:center; gap:12px;">
        <p style="color:var(--muted); font-family:var(--font);">Click &quot;Generate QR Code&quot; to see your QR code here.</p>
      </div>"""
    
    new_form = """      <h3>Try the """ + name + """</h3>
      <label for="apiInput">Input Value</label>
      <input type="text" id="apiInput" value="test" placeholder="Enter input...">
      <button class="btn" onclick="callAPI()">Call API \u2192</button>
      <div class="result" id="apiResult"><p style="color:var(--muted);font-family:var(--font);">Click &quot;Call API&quot; to test the endpoint.</p></div>"""
    
    page = page.replace(qr_form, new_form)
    
    # -- Replace QR-specific JavaScript with generic API caller --
    qr_js = """function generateQR() {"""
    api_js = """function callAPI() {"""
    page = page.replace(qr_js, api_js)
    
    # The rest of the QR function body
    qr_body = """  const text = document.getElementById('qrText').value.trim();
  const format = document.getElementById('qrFormat').value;
  const size = document.getElementById('qrSize').value;
  const result = document.getElementById('qrResult');

  if (!text) {
    result.innerHTML = '<p style="color:var(--danger);font-family:var(--font);">Please enter text or a URL.</p>';
    return;
  }

  const apiUrl = `https://api.gadgethumans.com/qr?text=${encodeURIComponent(text)}&format=${format}&size=${size}`;

  if (format === 'svg') {
    fetch(apiUrl)
      .then(r => r.text())
      .then(svg => {
        result.innerHTML = `<div style="max-width:${size}px;margin:0 auto;">${svg}</div>
          <p style="font-family:var(--font);font-size:0.78rem;color:var(--muted);">SVG format — scales infinitely</p>`;
      })
      .catch(() => {
        result.innerHTML = '<p style="color:var(--danger);font-family:var(--font);">Error generating QR code. Try again.</p>';
      });
  } else {
    result.innerHTML = `<img src="${apiUrl}" alt="QR Code" style="max-width:${size}px;border-radius:8px;">
      <p style="font-family:var(--font);font-size:0.78rem;color:var(--muted);">${format.toUpperCase()} — ${size}×${size}px</p>
      <a href="${apiUrl}" target="_blank" style="padding:6px 16px;background:var(--accent);color:#fff;border-radius:980px;text-decoration:none;font-size:0.8rem;font-weight:600;">Open in new tab →</a>`;
  }
}"""
    
    new_api_body = """  var input = document.getElementById('apiInput').value.trim();
  var result = document.getElementById('apiResult');
  if (!input) {
    result.innerHTML = '<p style="color:var(--danger);font-family:var(--font);">Please enter a value.</p>';
    return;
  }
  var apiUrl = 'https://api.gadgethumans.com""" + endpoint_path + """?value=' + encodeURIComponent(input);
  fetch(apiUrl)
    .then(function(r){ return r.json(); })
    .then(function(data){
      result.innerHTML = '<pre style="white-space:pre-wrap;word-break:break-all;font-size:0.82rem;color:var(--accent);margin:0;">' + JSON.stringify(data, null, 2) + '</pre>';
    })
    .catch(function(err){
      result.innerHTML = '<p style="color:var(--danger);font-family:var(--font);">Error calling API. Endpoint may be in development.</p>';
    });
}"""
    
    page = page.replace(qr_body, new_api_body)
    
    # Write page
    dir_path = os.path.join(BASE, "tools", slug)
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, "index.html"), "w") as f:
        f.write(page)
    print("Created " + slug + "/index.html")

print("\nDone! All 20 tool pages generated.")
