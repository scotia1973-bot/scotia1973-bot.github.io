#!/usr/bin/env python3
"""Generate 20 SEO tool landing pages for GadgetHumans."""
import os

BASE = "/Users/scottwishart/scotia1973-bot.github.io"
CSS_PATH = "../../css/theme.css?v=3"
JS_PATH = "../../js/liquid-glass.js"
SCRIPT_JS = "../../js/script.js"

TOOLS = [
    {
        "path": "qr-code",
        "emoji": "📱",
        "title": "QR Code Generator API",
        "h1": "QR Code Generator API",
        "desc": "Free QR Code Generator API. Generate QR codes from URLs, text, or any data. REST API with PNG, SVG support. No API key needed for free tier. 100 requests/day free.",
        "og_title": "QR Code Generator API — Free QR Code REST API",
        "og_desc": "Generate QR codes from any text or URL. Free REST API, no signup needed. PNG, SVG, GIF output. Custom colors and sizes.",
        "endpoint": "https://api.gadgethumans.com/qr",
        "endpoint_path": "/qr",
        "content_intro": "The GadgetHumans QR Code Generator API is a free, no-signup REST API that lets you generate QR codes programmatically. Whether you need to encode URLs, plain text, contact information, or Wi-Fi credentials into a QR code, this API handles it with a single HTTP GET request.",
        "content_detail": "With support for multiple output formats (PNG, SVG, GIF), customizable colors, adjustable error correction levels (L, M, Q, H), and configurable image sizes from 100 to 1000 pixels, this API is perfect for developers building web applications, mobile apps, marketing tools, inventory systems, or any project that requires on-the-fly QR code generation. The free tier offers 100 requests per day with no API key required, making it ideal for prototyping, small projects, and personal use.",
        "features": [
            ("100% Free Tier", "No API key, no signup, no credit card. Just make a GET request."),
            ("Multiple Formats", "Output in PNG (raster), SVG (vector), or GIF (animated). SVG is perfect for print and high-resolution displays."),
            ("Customizable Colors", "Set foreground and background colors using hex values. Match your brand colors effortlessly."),
            ("Adjustable Error Correction", "Choose from L (low, ~7%), M (medium, ~15%), Q (quartile, ~25%), or H (high, ~30%). Higher levels allow scanning even if the code is partially damaged."),
            ("Configurable Size", "Generate codes from 100px to 1000px. Control the margin (quiet zone) around the code."),
            ("Edge-Deployed", "Powered by Cloudflare Workers with 320+ global edge locations. Sub-50ms response times worldwide."),
        ],
        "faq": [
            ("Do I need an API key to use the QR code API?", "No! The free tier requires no API key or signup. Just send a GET request and receive your QR code. For the Pro tier, you'll get a dedicated API key for higher limits."),
            ("What output formats are supported?", "The API supports PNG (default), SVG (vector), and GIF formats. Use the format parameter to choose your preferred output."),
            ("Can I customize the colors of my QR code?", "Yes! Use the color parameter for the foreground (default: black) and bgcolor for the background (default: white). Both accept hex values without the # symbol."),
            ("What is the maximum text length I can encode?", "The API can encode up to 4,296 alphanumeric characters or 7,089 numeric characters, depending on the error correction level selected."),
            ("How many requests can I make on the free tier?", "The free tier allows up to 100 requests per day per IP address. For higher limits, subscribe to the Pro plan for $5/month, which gives you 10,000 requests per day."),
        ],
        "related": [
            ("password", "🔑", "Secure Password Generator", "Generate secure random passwords"),
            ("uuid", "🎲", "UUID Generator", "v4 unique identifiers"),
            ("hash", "📁", "Hash Generator", "MD5, SHA-1/256/512"),
            ("base64", "🔤", "Base64 Encode/Decode", "Encode & decode text"),
        ],
        "curl_code": '# Generate a QR code and save as PNG\ncurl "https://api.gadgethumans.com/qr?text=https://example.com&format=png&size=300" > qr.png\n\n# Get SVG output\ncurl "https://api.gadgethumans.com/qr?text=https://example.com&format=svg"',
        "python_code": 'import requests\n\n# Generate QR code\nurl = "https://api.gadgethumans.com/qr"\nparams = {\n    "text": "https://example.com",\n    "format": "png",\n    "size": "300",\n    "color": "000000",\n    "bgcolor": "FFFFFF"\n}\nresponse = requests.get(url, params=params)\n\n# Save to file\nwith open("qrcode.png", "wb") as f:\n    f.write(response.content)\nprint(f"QR code saved! Status: {response.status_code}")',
        "js_code": '// Generate QR code from browser\nconst url = `https://api.gadgethumans.com/qr?text=${encodeURIComponent("https://example.com")}&format=png&size=300`;\n\n// Display the QR code image\nconst img = document.createElement("img");\nimg.src = url;\nimg.alt = "QR Code";\ndocument.body.appendChild(img);',
    },
    {
        "path": "password",
        "emoji": "🔐",
        "title": "Secure Password Generator API",
        "h1": "Secure Password Generator API",
        "desc": "Free Password Generator API. Generate cryptographically secure random passwords with configurable length, symbols, numbers, and uppercase letters. REST API, no key needed.",
        "og_title": "Secure Password Generator API — Free Random Password REST API",
        "og_desc": "Generate secure random passwords via REST API. Configurable length, symbols, numbers, uppercase. Free tier, no signup. Perfect for developers and system admins.",
        "endpoint": "https://api.gadgethumans.com/password",
        "endpoint_path": "/password",
        "content_intro": "The GadgetHumans Secure Password Generator API is a free REST API that generates cryptographically secure random passwords on demand. Whether you need temporary credentials for new user accounts, API keys, one-time passwords, or just a strong password for your own accounts, this API delivers with a single HTTP GET request.",
        "content_detail": "You can fully customize the generated passwords: set the exact length (from 4 to 256 characters), include or exclude numbers, symbols, uppercase and lowercase letters. Generate one password or up to 50 at once. Each password is generated using cryptographically secure random number generation, ensuring true randomness that cannot be predicted. The free tier offers 100 requests per day with no API key required, making it ideal for development, testing, and personal automation. For production workloads, upgrade to the Pro tier for higher limits and dedicated API key access.",
        "features": [
            ("Cryptographically Secure", "Uses secure random number generation — passwords cannot be predicted or reverse-engineered."),
            ("Fully Configurable", "Control length (4-256), character sets — numbers, symbols, uppercase, lowercase."),
            ("Batch Generation", "Generate up to 50 passwords in a single request. Perfect for bulk user creation."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Edge-Deployed", "Cloudflare Workers with 320+ global edge locations. Blazing fast response times."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key and priority support."),
        ],
        "faq": [
            ("Do I need an API key?", "No! The free tier requires no API key or signup. Just send a GET request to start generating passwords."),
            ("How long can passwords be?", "You can set the length from 4 to 256 characters. The default is 16 characters."),
            ("Can I generate multiple passwords at once?", "Yes! Use the count parameter to generate up to 50 passwords in a single request."),
            ("Are the passwords truly random?", "Yes, the API uses cryptographically secure pseudo-random number generation (CSPRNG), suitable for passwords and security credentials."),
            ("What character sets can I include?", "You can independently toggle numbers (0-9), symbols (!@#$%^&*), uppercase (A-Z), and lowercase (a-z)."),
        ],
        "related": [
            ("uuid", "🎲", "UUID Generator", "v4 unique identifiers"),
            ("hash", "📁", "Hash Generator", "MD5, SHA-1/256/512"),
            ("base64", "🔤", "Base64 Encode/Decode", "Encode & decode text"),
            ("qr-code", "📱", "QR Code Generator", "QR codes from URLs and text"),
        ],
        "curl_code": '# Generate a 20-character password with all character types\ncurl "https://api.gadgethumans.com/password?length=20&numbers=true&symbols=true&uppercase=true&lowercase=true"\n\n# Generate 5 passwords at once\ncurl "https://api.gadgethumans.com/password?count=5&length=12"',
        "python_code": 'import requests\n\n# Generate a secure password\nurl = "https://api.gadgethumans.com/password"\nparams = {\n    "length": 20,\n    "numbers": "true",\n    "symbols": "true",\n    "uppercase": "true",\n    "lowercase": "true",\n    "count": 1\n}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"Generated password: {data["passwords"][0]}")',
        "js_code": '// Fetch a secure password from the API\nconst params = new URLSearchParams({\n    length: "20",\n    numbers: "true",\n    symbols: "true",\n    uppercase: "true",\n    lowercase: "true",\n    count: 1\n});\n\nfetch(`https://api.gadgethumans.com/password?${params}`)\n  .then(res => res.json())\n  .then(data => {\n    console.log("Generated password:", data.passwords[0]);\n    document.getElementById("password").textContent = data.passwords[0];\n  });',
    },
    {
        "path": "uuid",
        "emoji": "🎲",
        "title": "UUID Generator API",
        "h1": "UUID Generator API",
        "desc": "Free UUID Generator API. Generate random UUID v4 identifiers for database records, API resources, and session IDs. REST API, no API key required. Bulk generation supported.",
        "og_title": "UUID Generator API — Free UUID v4 REST API",
        "og_desc": "Generate UUID v4 identifiers via REST API. Bulk generation, JSON/array output formats. Free tier, no signup. Perfect for developers.",
        "endpoint": "https://api.gadgethumans.com/uuid",
        "endpoint_path": "/uuid",
        "content_intro": "The GadgetHumans UUID Generator API is a free REST API that generates universally unique identifiers (UUID v4) on demand. UUIDs are 128-bit identifiers that are globally unique, making them perfect for database primary keys, API resource identifiers, session tokens, transaction IDs, and any distributed system that needs collision-free identifiers.",
        "content_detail": "The API supports generating from 1 to 100 UUIDs in a single request, with multiple output formats including standard dashed format (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx), JSON array, and plain array. Each UUID is generated using cryptographically secure random number generation. The free tier offers 100 requests per day with no API key required, making it ideal for development, testing, and personal projects. For production workloads with higher throughput requirements, the Pro tier is available.",
        "features": [
            ("UUID v4 Standard", "Generates random UUIDs conforming to RFC 4122 Version 4. Globally unique, no central coordination needed."),
            ("Bulk Generation", "Generate up to 100 UUIDs in a single request. Perfect for seeding databases or batch operations."),
            ("Multiple Output Formats", "Choose from standard dashed format, JSON array, or plain text array output."),
            ("Cryptographically Secure", "Uses secure random generation — no predictability or collisions in practice."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Edge-Deployed", "Cloudflare Workers with 320+ global edge locations for minimal latency."),
        ],
        "faq": [
            ("What is a UUID v4?", "UUID v4 (Universally Unique Identifier version 4) is a 128-bit identifier generated using random numbers. It follows RFC 4122 and has virtually zero chance of collision."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup. Just send a GET request."),
            ("How many UUIDs can I generate at once?", "You can generate up to 100 UUIDs in a single request using the count parameter."),
            ("What output formats are available?", "You can choose between standard (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx), json (JSON array), or array (plain array) formats."),
            ("Are these UUIDs suitable for production?", "Yes, the UUIDs are generated using cryptographically secure randomness and are suitable for production use including database primary keys."),
        ],
        "related": [
            ("password", "🔑", "Secure Password Generator", "Generate secure random passwords"),
            ("hash", "📁", "Hash Generator", "MD5, SHA-1/256/512"),
            ("base64", "🔤", "Base64 Encode/Decode", "Encode & decode text"),
            ("random-generator", "🎲", "Random Generator", "Random numbers & data"),
        ],
        "curl_code": '# Generate a single UUID\ncurl "https://api.gadgethumans.com/uuid"\n\n# Generate 5 UUIDs as JSON array\ncurl "https://api.gadgethumans.com/uuid?count=5&format=json"',
        "python_code": 'import requests\n\n# Generate UUIDs\nurl = "https://api.gadgethumans.com/uuid"\nparams = {"count": 5, "format": "json"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"Generated {len(data["uuids"])} UUIDs:")\nfor uuid in data["uuids"]:\n    print(f"  - {uuid}")',
        "js_code": '// Fetch UUIDs from the API\nfetch("https://api.gadgethumans.com/uuid?count=3&format=json")\n  .then(res => res.json())\n  .then(data => {\n    console.log("Generated UUIDs:", data.uuids);\n    data.uuids.forEach(uuid => {\n      const li = document.createElement("li");\n      li.textContent = uuid;\n      document.getElementById("uuidList").appendChild(li);\n    });\n  });',
    },
    {
        "path": "hash",
        "emoji": "🔑",
        "title": "Hash Generator API — MD5, SHA-256, SHA-512",
        "h1": "Hash Generator API",
        "desc": "Free Hash Generator API. Generate MD5, SHA-1, SHA-256, and SHA-512 cryptographic hashes from any text. REST API for password hashing, data integrity, and digital signatures.",
        "og_title": "Hash Generator API — Free MD5, SHA-256, SHA-512 REST API",
        "og_desc": "Generate cryptographic hashes via REST API. Supports MD5, SHA-1, SHA-256, SHA-512. Hex or Base64 output. Free tier, no signup.",
        "endpoint": "https://api.gadgethumans.com/hash",
        "endpoint_path": "/hash",
        "content_intro": "The GadgetHumans Hash Generator API is a free REST API that computes cryptographic hashes of any input text. Supporting MD5, SHA-1, SHA-256, and SHA-512 algorithms, this API is essential for password storage, data integrity verification, digital signatures, checksums, and any scenario requiring a one-way hash function.",
        "content_detail": "You can choose between hex and base64 output encoding depending on your use case. SHA-256 and SHA-512 are recommended for security-sensitive applications, while MD5 and SHA-1 are suitable for checksums, deduplication, and non-security use cases. The free tier offers 100 requests per day with no API key required, making it perfect for developers needing quick hash computation in their applications, CI/CD pipelines, or data processing workflows.",
        "features": [
            ("Multiple Algorithms", "MD5, SHA-1, SHA-256, and SHA-512 — choose the right hash for your use case."),
            ("Flexible Output Encoding", "Output in hex (default) or base64 encoding to match your application needs."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Security Best Practices", "SHA-256 and SHA-512 recommended for security. MD5/SHA-1 for checksums and legacy systems."),
            ("Edge-Deployed", "Cloudflare Workers with 320+ global edge locations for minimal latency."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What hash algorithms are supported?", "The API supports MD5 (128-bit), SHA-1 (160-bit), SHA-256 (256-bit), and SHA-512 (512-bit)."),
            ("Which algorithm should I use for passwords?", "For password hashing, use SHA-256 or SHA-512. For production systems, consider using bcrypt or Argon2 for password storage specifically."),
            ("Can I get output in Base64 instead of hex?", "Yes! Use the encoding parameter set to base64 to get Base64-encoded hash output."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("What is the maximum input length?", "The API can hash text inputs of any reasonable length. For very large inputs, consider splitting into chunks."),
        ],
        "related": [
            ("password", "🔑", "Secure Password Generator", "Generate secure random passwords"),
            ("base64", "🔤", "Base64 Encode/Decode", "Encode & decode text"),
            ("uuid", "🎲", "UUID Generator", "v4 unique identifiers"),
            ("json", "📋", "JSON Formatter", "Prettify, validate, minify JSON"),
        ],
        "curl_code": '# Generate SHA-256 hash in hex\ncurl "https://api.gadgethumans.com/hash?text=hello%20world&algorithm=sha256"\n\n# Generate MD5 hash in base64\ncurl "https://api.gadgethumans.com/hash?text=hello%20world&algorithm=md5&encoding=base64"',
        "python_code": 'import requests\n\n# Hash text with SHA-256\nurl = "https://api.gadgethumans.com/hash"\nparams = {\n    "text": "Hello, World!",\n    "algorithm": "sha256",\n    "encoding": "hex"\n}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"SHA-256 hash: {data["hash"]}")',
        "js_code": '// Compute a hash from the browser\nconst text = "Hello, World!";\nconst algo = "sha256";\n\nfetch(`https://api.gadgethumans.com/hash?text=${encodeURIComponent(text)}&algorithm=${algo}`)\n  .then(res => res.json())\n  .then(data => {\n    console.log(`${algo} hash:`, data.hash);\n    document.getElementById("hashResult").textContent = data.hash;\n  });',
    },
    {
        "path": "base64",
        "emoji": "🔤",
        "title": "Base64 Encode/Decode API",
        "h1": "Base64 Encode/Decode API",
        "desc": "Free Base64 Encode and Decode API. Encode text to Base64 or decode Base64 back to text. REST API for data transport, email encoding, and API payloads.",
        "og_title": "Base64 Encode/Decode API — Free REST API",
        "og_desc": "Encode and decode Base64 via REST API. Perfect for data transport, email encoding, JSON payloads, and more. Free tier, no signup.",
        "endpoint": "https://api.gadgethumans.com/base64",
        "endpoint_path": "/base64",
        "content_intro": "The GadgetHumans Base64 Encode/Decode API is a free REST API that converts text to Base64 encoding and decodes Base64 strings back to plain text. Base64 encoding is essential for safely transmitting binary data over text-based protocols like HTTP, embedding images in HTML/CSS, encoding binary data in JSON payloads, and email attachments (MIME).",
        "content_detail": "With a single HTTP GET request, you can encode any text to Base64 or decode any valid Base64 string back to its original form. The API handles all padding and character set requirements automatically. The free tier offers 100 requests per day with no API key required, making it ideal for developers building integrations, processing API payloads, debugging encoded data, or working with data pipelines. For higher throughput requirements, the Pro tier is available.",
        "features": [
            ("Encode & Decode", "Convert text to Base64 and decode Base64 back to text with a single API call."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Simple REST API", "GET-based API with intuitive parameters. Works with any HTTP client."),
            ("Edge-Deployed", "Cloudflare Workers with 320+ global edge locations for minimal latency."),
            ("Auto Padding", "Handles Base64 padding automatically. Decodes both padded and unpadded input."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What is Base64 encoding used for?", "Base64 encodes binary data into ASCII text for safe transport over text-based protocols like HTTP, JSON, email, and XML."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("Can I decode any Base64 string?", "Yes, the API handles standard Base64 strings with or without padding characters (=)."),
            ("Is the encoding URL-safe?", "The API returns standard Base64 encoding. For URL-safe Base64 (using - and _ instead of + and /), you can post-process the output."),
            ("What happens if I try to decode invalid Base64?", "The API will return an error message indicating the input is not valid Base64."),
        ],
        "related": [
            ("hash", "🔑", "Hash Generator", "MD5, SHA-1/256/512"),
            ("json", "📋", "JSON Formatter", "Prettify, validate, minify JSON"),
            ("password", "🔐", "Secure Password Generator", "Generate secure random passwords"),
            ("case-converter", "🔤", "Text Case Converter", "UPPER, lower, Title, Sentence"),
        ],
        "curl_code": '# Encode text to Base64\ncurl "https://api.gadgethumans.com/base64?text=Hello%20World&mode=encode"\n\n# Decode Base64 back to text\ncurl "https://api.gadgethumans.com/base64?text=SGVsbG8gV29ybGQ=&mode=decode"',
        "python_code": 'import requests\n\n# Encode text to Base64\nurl = "https://api.gadgethumans.com/base64"\nparams = {"text": "Hello, World!", "mode": "encode"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"Encoded: {data["result"]}")\n\n# Decode it back\nparams["mode"] = "decode"\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"Decoded: {data["result"]}")',
        "js_code": '// Base64 encode from the browser\nconst text = "Hello, World!";\nfetch(`https://api.gadgethumans.com/base64?text=${encodeURIComponent(text)}&mode=encode`)\n  .then(res => res.json())\n  .then(data => {\n    console.log("Encoded:", data.result);\n    document.getElementById("result").textContent = data.result;\n  });',
    },
    {
        "path": "json",
        "emoji": "📋",
        "title": "JSON Prettify, Validate & Minify API",
        "h1": "JSON Prettify, Validate & Minify API",
        "desc": "Free JSON Prettify and Validate API. Prettify, minify, or validate JSON strings via REST. Perfect for API debugging, configuration formatting, and data processing.",
        "og_title": "JSON Prettify & Validate API — Free JSON REST API",
        "og_desc": "Prettify, validate, and minify JSON via REST API. Free tier, no signup. Perfect for developers needing JSON processing in their applications.",
        "endpoint": "https://api.gadgethumans.com/json",
        "endpoint_path": "/json",
        "content_intro": "The GadgetHumans JSON Prettify, Validate & Minify API is a free REST API that processes JSON strings programmatically. Whether you need to format (prettify) messy JSON for readability, validate that a string is syntactically correct JSON, or minify JSON to save bandwidth, this API handles it all with a single HTTP request.",
        "content_detail": "The prettify mode indents JSON with proper formatting and sorts keys alphabetically for consistent output. The validate mode checks JSON syntax and returns a pass/fail result. The minify mode strips all unnecessary whitespace for compact output ideal for storage and transmission. The free tier offers 100 requests per day with no API key required, making it perfect for API integrations, CI/CD pipelines, configuration file processing, and data transformation workflows.",
        "features": [
            ("Three Modes", "Prettify (format + sort keys), Validate (syntax check), and Minify (strip whitespace)."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Developer Friendly", "Simple GET-based API. Test directly in your browser or with any HTTP client."),
            ("Error Reporting", "Clear error messages when JSON is invalid, showing the specific parsing issue."),
            ("Edge-Deployed", "Cloudflare Workers with 320+ global edge locations for minimal latency."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What modes does the API support?", "The API supports three modes: prettify (format with indentation and sorted keys), validate (check syntax only), and minify (compact, no whitespace)."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("How do I pass JSON in a GET request?", "URL-encode the JSON string and pass it as the json_string parameter."),
            ("Does prettify sort object keys?", "Yes, the prettify mode sorts keys alphabetically for consistent, predictable output."),
            ("What happens if I pass invalid JSON?", "The validate mode will return an error with details about the parsing failure. The prettify and minify modes will also return error messages."),
        ],
        "related": [
            ("base64", "🔤", "Base64 Encode/Decode", "Encode & decode text"),
            ("hash", "🔑", "Hash Generator", "MD5, SHA-1/256/512"),
            ("case-converter", "🔤", "Text Case Converter", "UPPER, lower, Title, Sentence"),
            ("morse-code", "📡", "Morse Code Converter", "Text to Morse code"),
        ],
        "curl_code": '# Prettify JSON\ncurl -X POST "https://api.gadgethumans.com/json" \\\n  -H "Content-Type: application/json" \\\n  -d \'{"json_string":"{\\"name\\":\\"John\\",\\"age\\":30}","mode":"prettify"}\'\n\n# Validate JSON\ncurl "https://api.gadgethumans.com/json?json_string=%7B%22name%22%3A%22John%22%7D&mode=validate"',
        "python_code": 'import requests\nimport json\n\n# Prettify JSON\nurl = "https://api.gadgethumans.com/json"\nmessy_json = \'{"name":"John","age":30,"city":"New York"}\'\nparams = {"json_string": messy_json, "mode": "prettify"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(data["result"])',
        "js_code": '// Prettify JSON from the browser\nconst jsonStr = \'{"name":"John","age":30,"city":"New York"}\';\nfetch(`https://api.gadgethumans.com/json?json_string=${encodeURIComponent(jsonStr)}&mode=prettify`)\n  .then(res => res.json())\n  .then(data => {\n    console.log("Formatted JSON:", data.result);\n    document.getElementById("jsonResult").textContent = data.result;\n  });',
    },
    {
        "path": "color",
        "emoji": "🎨",
        "title": "Color Converter API — HEX to RGB",
        "h1": "Color Converter API",
        "desc": "Free Color Converter API. Convert between HEX and RGB color formats instantly. REST API for CSS colors, design systems, and web development.",
        "og_title": "Color Converter API — Free HEX to RGB REST API",
        "og_desc": "Convert colors between HEX and RGB formats via REST API. Perfect for CSS, design systems, and web development. Free tier, no signup.",
        "endpoint": "https://api.gadgethumans.com/color",
        "endpoint_path": "/color",
        "content_intro": "The GadgetHumans Color Converter API is a free REST API that converts color values between HEX (hexadecimal) and RGB (red, green, blue) formats. Perfect for web developers, designers, and anyone working with CSS colors who needs to translate between color representations programmatically.",
        "content_detail": "Convert HEX colors like #FF0000 to rgb(255, 0, 0) and back again with a single API call. The API accepts HEX values with or without the # prefix, and RGB values in standard CSS format or as comma-separated numbers. The free tier offers 100 requests per day with no API key required, making it ideal for design tool integrations, CSS preprocessing, CMS color pickers, and automated design workflows where color format conversion is needed at scale.",
        "features": [
            ("HEX to RGB", "Convert any HEX color (with or without #) to its RGB equivalent."),
            ("RGB to HEX", "Convert RGB values back to HEX format for web-safe color specification."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Flexible Input", "HEX with/without #, RGB as rgb(r,g,b) or comma-separated values."),
            ("Edge-Deployed", "Cloudflare Workers with 320+ global edge locations for minimal latency."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What color formats are supported?", "The API supports HEX (e.g., #FF0000 or FF0000) and RGB (e.g., rgb(255, 0, 0) or 255,0,0)."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("Can I convert multiple colors at once?", "The API processes one color per request. For batch conversion, make multiple requests."),
            ("Does the HEX value need the # prefix?", "No, the API accepts HEX values both with and without the # prefix."),
            ("What about HSL or other formats?", "Currently the API supports HEX and RGB. Other formats may be added in future releases."),
        ],
        "related": [
            ("json", "📋", "JSON Formatter", "Prettify, validate, minify JSON"),
            ("base64", "🔤", "Base64 Encode/Decode", "Encode & decode text"),
            ("unit-converter", "📐", "Unit Converter", "Length, weight, temperature"),
            ("case-converter", "🔤", "Text Case Converter", "UPPER, lower, Title, Sentence"),
        ],
        "curl_code": '# Convert HEX to RGB\ncurl "https://api.gadgethumans.com/color?value=%23FF0000&from_format=hex&to_format=rgb"\n\n# Convert RGB to HEX\ncurl "https://api.gadgethumans.com/color?value=rgb(255,0,0)&from_format=rgb&to_format=hex"',
        "python_code": 'import requests\n\n# Convert HEX to RGB\nurl = "https://api.gadgethumans.com/color"\nparams = {"value": "#FF0000", "from_format": "hex", "to_format": "rgb"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"HEX #FF0000 = RGB {data["result"]}")\n\n# Convert RGB to HEX\nparams = {"value": "rgb(255, 0, 0)", "from_format": "rgb", "to_format": "hex"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"RGB (255,0,0) = HEX {data["result"]}")',
        "js_code": '// Convert a color from the browser\nconst hexColor = "#FF0000";\nfetch(`https://api.gadgethumans.com/color?value=${encodeURIComponent(hexColor)}&from_format=hex&to_format=rgb`)\n  .then(res => res.json())\n  .then(data => {\n    console.log("RGB:", data.result);\n    document.getElementById("colorResult").textContent = data.result;\n  });',
    },
    {
        "path": "email-verify",
        "emoji": "✉️",
        "title": "Email Verification API",
        "h1": "Email Verification API",
        "desc": "Free Email Verification API. Validate email addresses in real-time — checks syntax, domain validity, and disposable email providers. REST API for form validation and list cleaning.",
        "og_title": "Email Verification API — Free Email Validation REST API",
        "og_desc": "Verify email addresses in real-time via REST API. Checks syntax, domain validity, and disposable email providers. Free tier, no signup.",
        "endpoint": "https://api.gadgethumans.com/email-verify",
        "endpoint_path": "/email-verify",
        "content_intro": "The GadgetHumans Email Verification API is a free REST API that validates email addresses in real-time. It verifies email format syntax, checks if the domain exists and can receive mail, and identifies disposable email providers. This API is essential for preventing fake signups, reducing bounce rates, and maintaining clean email lists.",
        "content_detail": "The API returns comprehensive validation results including whether the email is valid, deliverable, and from a disposable provider. Each check is performed in real-time against live DNS records and up-to-date disposable domain lists. The free tier offers 100 requests per day with no API key required, making it perfect for website registration forms, newsletter signups, contact forms, and data cleaning workflows where email validation is critical.",
        "features": [
            ("Syntax Validation", "Checks email format against RFC 5322 standards for proper structure."),
            ("Domain Verification", "Validates that the domain exists and has MX records for mail delivery."),
            ("Disposable Detection", "Identifies temporary and disposable email providers to prevent spam signups."),
            ("Real-time Results", "Instant validation with detailed status codes and explanations."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What checks does the API perform?", "The API checks email syntax, domain validity (DNS/MX records), and whether the address is from a known disposable email provider."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("Can I verify bulk email lists?", "The free tier supports 100 requests per day. For bulk verification, subscribe to the Pro tier."),
            ("How accurate is the verification?", "The API performs real-time checks against live DNS records for high accuracy. However, it cannot guarantee that an email inbox exists without sending a test email."),
            ("What is a disposable email provider?", "Disposable email providers offer temporary addresses (like Mailinator, Guerrilla Mail, Temp Mail) often used to bypass registration restrictions."),
        ],
        "related": [
            ("password", "🔐", "Secure Password Generator", "Generate secure random passwords"),
            ("uuid", "🎲", "UUID Generator", "v4 unique identifiers"),
            ("ip-geolocation", "🌍", "IP Geolocation API", "IP address location data"),
            ("geocoding", "📍", "Geocoding API", "Address to coordinates"),
        ],
        "curl_code": '# Verify an email address\ncurl "https://api.gadgethumans.com/email-verify?email=test@example.com"\n\n# Check a disposable email\ncurl "https://api.gadgethumans.com/email-verify?email=user@mailinator.com"',
        "python_code": 'import requests\n\n# Verify an email address\nurl = "https://api.gadgethumans.com/email-verify"\nparams = {"email": "user@example.com"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"Email: {data["email"]}")\nprint(f"Valid: {data["valid"]}")\nprint(f"Deliverable: {data["deliverable"]}")',
        "js_code": '// Verify an email from the browser\nconst email = "user@example.com";\nfetch(`https://api.gadgethumans.com/email-verify?email=${encodeURIComponent(email)}`)\n  .then(res => res.json())\n  .then(data => {\n    console.log("Verification result:", data);\n    document.getElementById("verifyResult").textContent = \n      data.valid ? "✅ Valid email" : "❌ Invalid email";\n  });',
    },
    {
        "path": "ip-geolocation",
        "emoji": "🌍",
        "title": "IP Geolocation API",
        "h1": "IP Geolocation API",
        "desc": "Free IP Geolocation API. Get geographic location, ISP, timezone, and more from any IP address. REST API for analytics, fraud detection, and geo-targeting.",
        "og_title": "IP Geolocation API — Free IP Location REST API",
        "og_desc": "Get geographic location data from any IP address via REST API. Country, city, ISP, timezone, and more. Free tier, no signup.",
        "endpoint": "https://api.gadgethumans.com/ip-geolocation",
        "endpoint_path": "/ip-geolocation",
        "content_intro": "The GadgetHumans IP Geolocation API is a free REST API that returns detailed geographic information for any IP address. Get country, city, region, latitude/longitude coordinates, ISP, timezone, and more with a single API call. Essential for analytics, fraud detection, content localization, and geo-targeting applications.",
        "content_detail": "The API works with both IPv4 and IPv6 addresses. If no IP address is provided, it returns data for the requester's own IP. Results include country code and name, city, region/state, postal code, latitude/longitude, timezone, ISP name, and ASN information. The free tier offers 100 requests per day with no API key required, making it ideal for web analytics, e-commerce fraud checks, content personalization, and debugging network issues.",
        "features": [
            ("Comprehensive Data", "Country, city, region, coordinates, timezone, ISP, ASN, and more."),
            ("IPv4 & IPv6", "Works with both IPv4 and IPv6 addresses."),
            ("Auto IP Detection", "Call without an IP to get the requesting client's location."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Low Latency", "Powered by Cloudflare Workers on the global edge network."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What data does the API return?", "Country, city, region, latitude/longitude, timezone, ISP, ASN, and postal code where available."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("Can I look up my own IP?", "Yes, simply omit the ip_address parameter or pass an empty string."),
            ("Does it support IPv6?", "Yes, the API supports both IPv4 and IPv6 address formats."),
            ("How accurate is the location data?", "IP geolocation accuracy varies by region. Country-level is highly accurate, city-level is typically accurate for major cities."),
        ],
        "related": [
            ("email-verify", "✉️", "Email Verification API", "Validate email addresses"),
            ("geocoding", "📍", "Geocoding API", "Address to coordinates"),
            ("weather", "⛅", "Weather API", "Current weather data"),
            ("timestamp", "🕐", "Timestamp Converter", "Unix to date conversion"),
        ],
        "curl_code": '# Look up an IP address\ncurl "https://api.gadgethumans.com/ip-geolocation?ip_address=8.8.8.8"\n\n# Get your own IP data\ncurl "https://api.gadgethumans.com/ip-geolocation"',
        "python_code": 'import requests\n\n# Get geolocation for an IP\nurl = "https://api.gadgethumans.com/ip-geolocation"\nparams = {"ip_address": "8.8.8.8"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"IP: {data["ip"]}")\nprint(f"Location: {data["city"]}, {data["country_name"]}")\nprint(f"ISP: {data["isp"]}")',
        "js_code": '// Look up IP geolocation\nconst ip = "8.8.8.8";\nfetch(`https://api.gadgethumans.com/ip-geolocation?ip_address=${ip}`)\n  .then(res => res.json())\n  .then(data => {\n    console.log("Location:", data.city, data.country_name);\n    document.getElementById("geoResult").textContent = \n      `${data.city}, ${data.country_name} - ${data.isp}`;\n  });',
    },
    {
        "path": "timestamp",
        "emoji": "🕐",
        "title": "Timestamp Converter API",
        "h1": "Timestamp Converter API",
        "desc": "Free Timestamp Converter API. Convert Unix timestamps to human-readable dates and back. REST API for developers working with epoch time and ISO 8601.",
        "og_title": "Timestamp Converter API — Free Unix Time REST API",
        "og_desc": "Convert Unix timestamps to dates and dates to timestamps via REST API. ISO 8601, RFC 2822, Unix formats. Free tier, no signup.",
        "endpoint": "https://api.gadgethumans.com/timestamp",
        "endpoint_path": "/timestamp",
        "content_intro": "The GadgetHumans Timestamp Converter API is a free REST API that converts between Unix epoch timestamps and human-readable date formats. Whether you need to convert a Unix timestamp (like 1717000000) to ISO 8601, or parse a date string back to a Unix timestamp, this API handles it instantly with a single HTTP request.",
        "content_detail": "The API accepts Unix timestamps in seconds since epoch, as well as various date string formats including ISO 8601 (2025-05-29T00:00:00Z), RFC 2822, and natural language dates. Output formats include iso, unix, rfc2822, and more. The free tier offers 100 requests per day with no API key required, making it perfect for developers debugging logs, working with database timestamps, building calendar applications, or processing time-series data from APIs that use epoch time.",
        "features": [
            ("Unix to Date", "Convert epoch timestamps to ISO 8601, RFC 2822, and other human-readable formats."),
            ("Date to Unix", "Parse date strings back to Unix timestamps for database and API use."),
            ("Multiple Formats", "ISO 8601, RFC 2822, Unix, and more output formats available."),
            ("Flexible Input", "Accepts Unix timestamps, ISO 8601, RFC 2822, and many common date formats."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What input formats are accepted?", "Unix timestamps (seconds since epoch), ISO 8601 (2025-05-29), RFC 2822, and many common date formats."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("What output formats are supported?", "iso (ISO 8601), unix (epoch seconds), rfc2822, and other standard date formats."),
            ("Does it handle timezones?", "The API returns UTC by default. Specify timezone offsets in the input for localized conversions."),
            ("Can I convert milliseconds timestamps?", "The API uses seconds since epoch. Divide milliseconds by 1000 before passing to the API."),
        ],
        "related": [
            ("ip-geolocation", "🌍", "IP Geolocation API", "IP address location data"),
            ("weather", "⛅", "Weather API", "Current weather data"),
            ("currency", "💱", "Currency Converter", "Exchange rates and conversion"),
            ("geocoding", "📍", "Geocoding API", "Address to coordinates"),
        ],
        "curl_code": '# Convert Unix timestamp to ISO 8601\ncurl "https://api.gadgethumans.com/timestamp?value=1717000000&format=iso"\n\n# Convert date string to Unix\ncurl "https://api.gadgethumans.com/timestamp?value=2025-05-29&format=unix"',
        "python_code": 'import requests\n\n# Convert Unix timestamp to ISO date\nurl = "https://api.gadgethumans.com/timestamp"\nparams = {"value": "1717000000", "format": "iso"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"Unix 1717000000 = {data["result"]}")\n\n# Convert date to Unix\nparams = {"value": "2025-05-29", "format": "unix"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"2025-05-29 = Unix {data["result"]}")',
        "js_code": '// Convert a timestamp from the browser\nconst timestamp = "1717000000";\nfetch(`https://api.gadgethumans.com/timestamp?value=${timestamp}&format=iso`)\n  .then(res => res.json())\n  .then(data => {\n    console.log("ISO date:", data.result);\n    document.getElementById("tsResult").textContent = data.result;\n  });',
    },
    {
        "path": "lorem-ipsum",
        "emoji": "📄",
        "title": "Lorem Ipsum Generator API",
        "h1": "Lorem Ipsum Generator API",
        "desc": "Free Lorem Ipsum Generator API. Generate placeholder text in paragraphs, sentences, or words. REST API for design mockups, wireframes, and prototypes.",
        "og_title": "Lorem Ipsum Generator API — Free Placeholder Text REST API",
        "og_desc": "Generate Lorem Ipsum placeholder text via REST API. Paragraphs, sentences, or words. Perfect for mockups and wireframes. Free tier, no signup.",
        "endpoint": "https://api.gadgethumans.com/lorem-ipsum",
        "endpoint_path": "/lorem-ipsum",
        "content_intro": "The GadgetHumans Lorem Ipsum Generator API is a free REST API that generates Lorem Ipsum placeholder text on demand. Whether you need paragraphs for a design mockup, sentences for a wireframe, or just a few words for UI prototypes, this API delivers with a single HTTP GET request.",
        "content_detail": "Choose from three output types: paragraphs (full paragraph blocks with multiple sentences), sentences (individual sentences), or words (individual words). Control the quantity from 1 to 100 units. The generated text uses standard Lorem Ipsum text with pseudo-Latin roots. The free tier offers 100 requests per day with no API key required, making it perfect for designers, frontend developers, content strategists, and anyone creating mockups, templates, or layout prototypes that need realistic text placeholders.",
        "features": [
            ("Three Output Types", "Paragraphs, sentences, or words — choose the right unit for your need."),
            ("Configurable Count", "Generate from 1 to 100 units in a single request."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Quick Integration", "Simple GET-based API. Works with any programming language or HTTP client."),
            ("Edge-Deployed", "Powered by Cloudflare Workers on the global edge network."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What types of output are available?", "You can generate paragraphs, sentences, or words of Lorem Ipsum text."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("How many units can I generate at once?", "You can generate between 1 and 100 units per request."),
            ("Is the text real Latin?", "No, Lorem Ipsum is derived from Latin but uses scrambled, modified text that doesn't form coherent sentences. It's designed to look like natural text for layout testing."),
            ("Can I use this in commercial projects?", "Yes, the generated text is free to use in any project, commercial or personal."),
        ],
        "related": [
            ("case-converter", "🔤", "Text Case Converter", "UPPER, lower, Title, Sentence"),
            ("morse-code", "📡", "Morse Code Converter", "Text to Morse code"),
            ("nato-phonetic", "🔊", "NATO Phonetic Alphabet", "Text to NATO alphabet"),
            ("json", "📋", "JSON Formatter", "Prettify, validate, minify JSON"),
        ],
        "curl_code": '# Generate 3 paragraphs\ncurl "https://api.gadgethumans.com/lorem-ipsum?type=paragraphs&count=3"\n\n# Generate 5 sentences\ncurl "https://api.gadgethumans.com/lorem-ipsum?type=sentences&count=5"\n\n# Generate 10 words\ncurl "https://api.gadgethumans.com/lorem-ipsum?type=words&count=10"',
        "python_code": 'import requests\n\n# Generate Lorem Ipsum placeholder text\nurl = "https://api.gadgethumans.com/lorem-ipsum"\nparams = {"type": "paragraphs", "count": 3}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(data["text"])',
        "js_code": '// Fetch Lorem Ipsum text from the browser\nfetch("https://api.gadgethumans.com/lorem-ipsum?type=paragraphs&count=2")\n  .then(res => res.json())\n  .then(data => {\n    console.log("Generated text:", data.text);\n    document.getElementById("loremResult").textContent = data.text;\n  });',
    },
    {
        "path": "currency",
        "emoji": "💱",
        "title": "Currency Converter API",
        "h1": "Currency Converter API",
        "desc": "Free Currency Converter API. Get real-time exchange rates and convert between 170+ currencies. REST API for e-commerce, finance apps, and travel tools.",
        "og_title": "Currency Converter API — Free Exchange Rate REST API",
        "og_desc": "Convert between 170+ currencies with real-time exchange rates via REST API. Perfect for e-commerce, finance, and travel apps. Free tier, no signup.",
        "endpoint": "https://api.gadgethumans.com/currency",
        "endpoint_path": "/currency",
        "content_intro": "The GadgetHumans Currency Converter API is a free REST API that provides real-time exchange rates and currency conversion for over 170 currencies worldwide. Whether you're building an e-commerce platform, a financial dashboard, a travel expense tracker, or a price comparison tool, this API delivers accurate exchange rates with a single HTTP request.",
        "content_detail": "Convert any amount from one currency to another using real-time exchange rates. The API supports all major world currencies including USD, EUR, GBP, JPY, CAD, AUD, CNY, and hundreds more using standard ISO 4217 currency codes. The free tier offers 100 requests per day with no API key required, making it ideal for development, personal finance tools, travel apps, and small business applications that need up-to-date currency conversion.",
        "features": [
            ("170+ Currencies", "Support for all major world currencies using ISO 4217 three-letter codes."),
            ("Real-time Rates", "Live exchange rates updated frequently from reliable financial data sources."),
            ("Any Amount", "Convert any monetary amount between any pair of supported currencies."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Edge-Deployed", "Cloudflare Workers with 320+ global edge locations for minimal latency."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("How many currencies are supported?", "The API supports over 170 currencies from around the world, including all major fiat currencies."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("How often are exchange rates updated?", "Rates are updated multiple times per day from financial data providers."),
            ("What currency codes should I use?", "Use standard ISO 4217 three-letter codes like USD, EUR, GBP, JPY, etc."),
            ("Can I get a list of supported currencies?", "The API returns the source and target currencies with each conversion result."),
        ],
        "related": [
            ("unit-converter", "📐", "Unit Converter", "Length, weight, temperature"),
            ("timestamp", "🕐", "Timestamp Converter", "Unix to date conversion"),
            ("weather", "⛅", "Weather API", "Current weather data"),
            ("geocoding", "📍", "Geocoding API", "Address to coordinates"),
        ],
        "curl_code": '# Convert 100 USD to EUR\ncurl "https://api.gadgethumans.com/currency?from=USD&to=EUR&amount=100"\n\n# Convert 50 GBP to JPY\ncurl "https://api.gadgethumans.com/currency?from=GBP&to=JPY&amount=50"',
        "python_code": 'import requests\n\n# Convert currency\nurl = "https://api.gadgethumans.com/currency"\nparams = {"from": "USD", "to": "EUR", "amount": 100}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"100 USD = {data["result"]} EUR")',
        "js_code": '// Convert currency from the browser\nfetch("https://api.gadgethumans.com/currency?from=USD&to=EUR&amount=100")\n  .then(res => res.json())\n  .then(data => {\n    console.log("100 USD =", data.result, "EUR");\n    document.getElementById("currencyResult").textContent = \n      `100 USD = ${data.result} EUR`;\n  });',
    },
    {
        "path": "weather",
        "emoji": "⛅",
        "title": "Weather API",
        "h1": "Weather API",
        "desc": "Free Weather API. Get current weather conditions, temperature, humidity, wind speed, and more for any city. REST API for weather apps and dashboards.",
        "og_title": "Weather API — Free Current Weather REST API",
        "og_desc": "Get current weather data for any city via REST API. Temperature, humidity, wind, conditions. Free tier, no signup. Perfect for weather apps.",
        "endpoint": "https://api.gadgethumans.com/weather",
        "endpoint_path": "/weather",
        "content_intro": "The GadgetHumans Weather API is a free REST API that returns current weather conditions for any city worldwide. Get temperature, feels-like temperature, humidity, wind speed and direction, weather description, and atmospheric pressure with a single HTTP GET request.",
        "content_detail": "Search by city name and optionally by country code for disambiguation. The API returns detailed current conditions including temperature in Celsius, weather icon codes, cloud cover percentage, visibility, and more. The free tier offers 100 requests per day with no API key required, making it ideal for weather dashboards, travel apps, smart home integrations, agriculture monitoring, and any application that needs real-time weather data without complex setup.",
        "features": [
            ("Current Conditions", "Temperature, humidity, wind, pressure, visibility, cloud cover, and more."),
            ("City Search", "Search by city name, optionally with country code for disambiguation."),
            ("Global Coverage", "Weather data for cities worldwide, from major metropolises to small towns."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Edge-Deployed", "Cloudflare Workers with 320+ global edge locations for minimal latency."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What weather data is returned?", "Temperature, feels-like temperature, humidity, wind speed/direction, weather description, pressure, visibility, and cloud cover."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("Can I search by ZIP code?", "Currently the API supports city name search. ZIP code search may be added in a future update."),
            ("How often is weather data updated?", "Weather data is refreshed from upstream providers every 10-15 minutes."),
            ("Does it support Fahrenheit?", "The API returns temperature in Celsius by default. Convert on the client side as needed."),
        ],
        "related": [
            ("ip-geolocation", "🌍", "IP Geolocation API", "IP address location data"),
            ("geocoding", "📍", "Geocoding API", "Address to coordinates"),
            ("currency", "💱", "Currency Converter", "Exchange rates and conversion"),
            ("timestamp", "🕐", "Timestamp Converter", "Unix to date conversion"),
        ],
        "curl_code": '# Get weather for London\ncurl "https://api.gadgethumans.com/weather?city=London&country=GB"\n\n# Get weather for New York\ncurl "https://api.gadgethumans.com/weather?city=New%20York&country=US"',
        "python_code": 'import requests\n\n# Get current weather\nurl = "https://api.gadgethumans.com/weather"\nparams = {"city": "London", "country": "GB"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"Weather in {data["city"]}, {data["country"]}:")\nprint(f"  Temperature: {data["temperature"]}°C")\nprint(f"  Conditions: {data["description"]}")\nprint(f"  Humidity: {data["humidity"]}%")',
        "js_code": '// Get weather from the browser\nconst city = "London";\nconst country = "GB";\nfetch(`https://api.gadgethumans.com/weather?city=${encodeURIComponent(city)}&country=${country}`)\n  .then(res => res.json())\n  .then(data => {\n    console.log("Weather:", data);\n    document.getElementById("weatherResult").innerHTML = \n      `${data.temperature}°C, ${data.description}`;\n  });',
    },
    {
        "path": "geocoding",
        "emoji": "📍",
        "title": "Geocoding API",
        "h1": "Geocoding API",
        "desc": "Free Geocoding API. Convert addresses to geographic coordinates (latitude/longitude) and reverse geocode coordinates back to addresses. REST API for maps and location services.",
        "og_title": "Geocoding API — Free Address to Coordinates REST API",
        "og_desc": "Convert addresses to coordinates and coordinates to addresses via REST API. Perfect for maps, logistics, and location-based services. Free tier, no signup.",
        "endpoint": "https://api.gadgethumans.com/geocoding",
        "endpoint_path": "/geocoding",
        "content_intro": "The GadgetHumans Geocoding API is a free REST API that converts addresses to geographic coordinates (forward geocoding) and coordinates back to addresses (reverse geocoding). Essential for mapping applications, logistics, delivery route planning, location-based services, and any application that needs to translate between human-readable addresses and map coordinates.",
        "content_detail": "Forward geocoding takes an address string (like '1600 Amphitheatre Parkway, Mountain View, CA') and returns latitude/longitude coordinates plus structured address components. Reverse geocoding takes coordinates (latitude, longitude) and returns the nearest address. The free tier offers 100 requests per day with no API key required, making it perfect for store locators, delivery apps, travel planners, and real estate applications that need geolocation capabilities.",
        "features": [
            ("Forward Geocoding", "Convert any address string to latitude/longitude coordinates."),
            ("Reverse Geocoding", "Convert latitude/longitude back to a human-readable address."),
            ("Structured Results", "Returns formatted address, street, city, state, postal code, country."),
            ("Global Coverage", "Address data for locations worldwide from major mapping data sources."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What is forward geocoding?", "Forward geocoding converts a human-readable address (e.g., '1600 Amphitheatre Pkwy, Mountain View, CA') into geographic coordinates (latitude and longitude)."),
            ("What is reverse geocoding?", "Reverse geocoding converts geographic coordinates back into a human-readable address."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("What format should coordinates be in?", "For reverse geocoding, pass coordinates as 'latitude,longitude' (e.g., '37.422,-122.084')."),
            ("How accurate is the address data?", "Accuracy varies by location. Major cities and well-known addresses typically return highly accurate results."),
        ],
        "related": [
            ("ip-geolocation", "🌍", "IP Geolocation API", "IP address location data"),
            ("weather", "⛅", "Weather API", "Current weather data"),
            ("currency", "💱", "Currency Converter", "Exchange rates and conversion"),
            ("timestamp", "🕐", "Timestamp Converter", "Unix to date conversion"),
        ],
        "curl_code": '# Forward geocode an address\ncurl "https://api.gadgethumans.com/geocoding?address=1600%20Amphitheatre%20Parkway%2C%20Mountain%20View%2C%20CA"\n\n# Reverse geocode coordinates\ncurl "https://api.gadgethumans.com/geocoding?lat=37.422&lon=-122.084"',
        "python_code": 'import requests\n\n# Forward geocode an address\nurl = "https://api.gadgethumans.com/geocoding"\nparams = {"address": "1600 Amphitheatre Parkway, Mountain View, CA"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"Coordinates: {data["lat"]}, {data["lon"]}")\nprint(f"Formatted: {data["formatted_address"]}")',
        "js_code": '// Geocode an address from the browser\nconst address = "1600 Amphitheatre Parkway, Mountain View, CA";\nfetch(`https://api.gadgethumans.com/geocoding?address=${encodeURIComponent(address)}`)\n  .then(res => res.json())\n  .then(data => {\n    console.log("Coordinates:", data.lat, data.lon);\n    document.getElementById("geoResult").textContent = \n      `Lat: ${data.lat}, Lon: ${data.lon}`;\n  });',
    },
    {
        "path": "unit-converter",
        "emoji": "📐",
        "title": "Unit Converter API",
        "h1": "Unit Converter API",
        "desc": "Free Unit Converter API. Convert between units of length, weight, temperature, volume, area, speed, and pressure. REST API for calculators and conversion tools.",
        "og_title": "Unit Converter API — Free Conversion REST API",
        "og_desc": "Convert between units of length, weight, temperature, volume, and more via REST API. Perfect for calculators and conversion tools. Free tier, no signup.",
        "endpoint": "https://api.gadgethumans.com/unit-converter",
        "endpoint_path": "/unit-converter",
        "content_intro": "The GadgetHumans Unit Converter API is a free REST API that converts measurements between different units across multiple categories including length, weight, temperature, volume, area, speed, and pressure. Essential for building calculator tools, educational apps, engineering software, cooking apps, and any application that needs unit conversion capabilities.",
        "content_detail": "Each category supports common units: length (meters, feet, inches, kilometers, miles), weight (kilograms, pounds, ounces, grams), temperature (Celsius, Fahrenheit, Kelvin), volume (liters, gallons, cups, milliliters), area (sq meters, sq feet, acres), speed (km/h, mph, knots), and pressure (Pa, psi, bar, atm). The free tier offers 100 requests per day with no API key required, making it perfect for developer tools, educational platforms, e-commerce size converters, and DIY calculator apps.",
        "features": [
            ("7 Conversion Categories", "Length, weight, temperature, volume, area, speed, and pressure."),
            ("30+ Supported Units", "Common units for every category including metric and imperial."),
            ("Precise Conversion", "Accurate conversion using standardized conversion factors."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Simple REST API", "GET-based API with intuitive parameters. Works with any HTTP client."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What conversion categories are supported?", "Length, weight/mass, temperature, volume, area, speed, and pressure."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("What units are available for temperature?", "Celsius (C), Fahrenheit (F), and Kelvin (K)."),
            ("Can I convert between metric and imperial?", "Yes, all categories support both metric and imperial units."),
            ("How precise are the conversions?", "Conversions use standard conversion factors with high precision arithmetic."),
        ],
        "related": [
            ("currency", "💱", "Currency Converter", "Exchange rates and conversion"),
            ("color", "🎨", "Color Converter", "HEX to RGB conversion"),
            ("timestamp", "🕐", "Timestamp Converter", "Unix to date conversion"),
            ("roman-numerals", "🏛️", "Roman Numeral Converter", "Numbers to Roman numerals"),
        ],
        "curl_code": '# Convert 5 feet to meters\ncurl "https://api.gadgethumans.com/unit-converter?category=length&from=feet&to=meters&value=5"\n\n# Convert 100 Fahrenheit to Celsius\ncurl "https://api.gadgethumans.com/unit-converter?category=temperature&from=fahrenheit&to=celsius&value=100"',
        "python_code": 'import requests\n\n# Convert feet to meters\nurl = "https://api.gadgethumans.com/unit-converter"\nparams = {"category": "length", "from": "feet", "to": "meters", "value": 5}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"5 feet = {data["result"]} meters")',
        "js_code": '// Convert units from the browser\nfetch("https://api.gadgethumans.com/unit-converter?category=length&from=feet&to=meters&value=5")\n  .then(res => res.json())\n  .then(data => {\n    console.log("5 feet =", data.result, "meters");\n    document.getElementById("convertResult").textContent = \n      `5 feet = ${data.result} meters`;\n  });',
    },
    {
        "path": "roman-numerals",
        "emoji": "🏛️",
        "title": "Roman Numeral Converter API",
        "h1": "Roman Numeral Converter API",
        "desc": "Free Roman Numeral Converter API. Convert numbers to Roman numerals and Roman numerals back to numbers. REST API for education, puzzles, and historical applications.",
        "og_title": "Roman Numeral Converter API — Free REST API",
        "og_desc": "Convert between numbers and Roman numerals via REST API. Supports 1 to 3999. Perfect for educational tools, history apps, and puzzles. Free tier, no signup.",
        "endpoint": "https://api.gadgethumans.com/roman-numerals",
        "endpoint_path": "/roman-numerals",
        "content_intro": "The GadgetHumans Roman Numeral Converter API is a free REST API that converts between standard numbers and Roman numerals. Convert any integer from 1 to 3999 to its Roman numeral equivalent (I, V, X, L, C, D, M) and parse Roman numerals back to numbers. Perfect for educational tools, history applications, puzzle games, and any project working with classic numbering systems.",
        "content_detail": "The API follows standard Roman numeral rules including subtractive notation (IV for 4, IX for 9, XL for 40, XC for 90, CD for 400, CM for 900). It handles the full range of 1 to 3999, which covers the standard Roman numeral representation range. The free tier offers 100 requests per day with no API key required, making it ideal for educational websites, history learning apps, clock and time-telling tools, and board game implementations that use Roman numerals.",
        "features": [
            ("Number to Roman", "Convert any integer (1-3999) to Roman numerals with proper subtractive notation."),
            ("Roman to Number", "Parse Roman numeral strings back to their integer values."),
            ("Standard Notation", "Uses standard Roman numeral rules including subtractive forms (IV, IX, XL, XC, CD, CM)."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Edge-Deployed", "Cloudflare Workers with 320+ global edge locations for minimal latency."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What range of numbers is supported?", "The API supports numbers from 1 to 3999, which is the standard range for Roman numeral representation."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("Does it use subtractive notation?", "Yes, the API uses standard subtractive notation including IV (4), IX (9), XL (40), XC (90), CD (400), and CM (900)."),
            ("Can I convert Roman numerals with lowercase letters?", "The API accepts both uppercase and lowercase Roman numeral input."),
            ("What happens if I enter an invalid Roman numeral?", "The API will return an error message indicating the input is not a valid Roman numeral."),
        ],
        "related": [
            ("unit-converter", "📐", "Unit Converter", "Length, weight, temperature"),
            ("timestamp", "🕐", "Timestamp Converter", "Unix to date conversion"),
            ("color", "🎨", "Color Converter", "HEX to RGB conversion"),
            ("morse-code", "📡", "Morse Code Converter", "Text to Morse code"),
        ],
        "curl_code": '# Convert number to Roman numeral\ncurl "https://api.gadgethumans.com/roman-numerals?value=2025&mode=to_roman"\n\n# Convert Roman numeral to number\ncurl "https://api.gadgethumans.com/roman-numerals?value=MMXXV&mode=from_roman"',
        "python_code": 'import requests\n\n# Convert number to Roman numeral\nurl = "https://api.gadgethumans.com/roman-numerals"\nparams = {"value": 2025, "mode": "to_roman"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"2025 = {data["result"]}")',
        "js_code": '// Convert a number to Roman numerals\nfetch("https://api.gadgethumans.com/roman-numerals?value=2025&mode=to_roman")\n  .then(res => res.json())\n  .then(data => {\n    console.log("2025 =", data.result);\n    document.getElementById("romanResult").textContent = `2025 = ${data.result}`;\n  });',
    },
    {
        "path": "case-converter",
        "emoji": "🔤",
        "title": "Text Case Converter API",
        "h1": "Text Case Converter API",
        "desc": "Free Text Case Converter API. Convert text to UPPERCASE, lowercase, Title Case, Sentence case, and more. REST API for text processing and content formatting.",
        "og_title": "Text Case Converter API — Free REST API",
        "og_desc": "Convert text between different cases via REST API. UPPERCASE, lowercase, Title Case, Sentence case, and more. Free tier, no signup.",
        "endpoint": "https://api.gadgethumans.com/case-converter",
        "endpoint_path": "/case-converter",
        "content_intro": "The GadgetHumans Text Case Converter API is a free REST API that transforms text between different letter cases. Convert to UPPERCASE, lowercase, Title Case, Sentence case, camelCase, PascalCase, snake_case, kebab-case, and more with a single HTTP GET request. Essential for content management, data normalization, code generation, and text processing pipelines.",
        "content_detail": "Each conversion mode handles edge cases intelligently: Title Case capitalizes major words while leaving articles and prepositions lowercase; Sentence Case capitalizes the first word of each sentence; camelCase and PascalCase handle multi-word conversions properly. The free tier offers 100 requests per day with no API key required, making it perfect for CMS integrations, SEO tools, data cleaning workflows, automated content generation, and developer tools that need consistent text formatting.",
        "features": [
            ("Multiple Cases", "UPPERCASE, lowercase, Title Case, Sentence case, camelCase, PascalCase, snake_case, kebab-case, and more."),
            ("Intelligent Conversion", "Smart handling of edge cases — Title Case skips articles, camelCase handles multi-word phrases."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Quick Integration", "Simple GET-based API with intuitive parameters."),
            ("Edge-Deployed", "Cloudflare Workers with 320+ global edge locations for minimal latency."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What case conversions are supported?", "UPPERCASE, lowercase, Title Case, Sentence case, camelCase, PascalCase, snake_case, kebab-case, and alternating case."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("How does Title Case handle articles?", "Title Case intelligently leaves articles (a, an, the), conjunctions (and, but, or), and short prepositions lowercase unless they're the first or last word."),
            ("Can I convert multiple strings at once?", "The API processes one text string per request. For batch conversion, make multiple requests."),
            ("What is camelCase vs PascalCase?", "camelCase starts with a lowercase letter (e.g., 'helloWorld'), while PascalCase starts with uppercase (e.g., 'HelloWorld')."),
        ],
        "related": [
            ("morse-code", "📡", "Morse Code Converter", "Text to Morse code"),
            ("nato-phonetic", "🔊", "NATO Phonetic Alphabet", "Text to NATO alphabet"),
            ("base64", "🔤", "Base64 Encode/Decode", "Encode & decode text"),
            ("lorem-ipsum", "📄", "Lorem Ipsum Generator", "Placeholder text generation"),
        ],
        "curl_code": '# Convert to Title Case\ncurl "https://api.gadgethumans.com/case-converter?text=hello%20world%20from%20the%20api&mode=title"\n\n# Convert to snake_case\ncurl "https://api.gadgethumans.com/case-converter?text=convert%20this%20text&mode=snake"',
        "python_code": 'import requests\n\n# Convert text case\nurl = "https://api.gadgethumans.com/case-converter"\nparams = {"text": "hello world from the api", "mode": "title"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"Title Case: {data["result"]}")',
        "js_code": '// Convert text case from the browser\nconst text = "hello world from the api";\nfetch(`https://api.gadgethumans.com/case-converter?text=${encodeURIComponent(text)}&mode=title`)\n  .then(res => res.json())\n  .then(data => {\n    console.log("Result:", data.result);\n    document.getElementById("caseResult").textContent = data.result;\n  });',
    },
    {
        "path": "morse-code",
        "emoji": "📡",
        "title": "Morse Code Converter API",
        "h1": "Morse Code Converter API",
        "desc": "Free Morse Code Converter API. Convert text to Morse code and decode Morse code back to text. REST API for education, radio enthusiasts, and signal processing.",
        "og_title": "Morse Code Converter API — Free REST API",
        "og_desc": "Convert text to Morse code and decode Morse code back to text via REST API. Supports A-Z, 0-9, and common punctuation. Free tier, no signup.",
        "endpoint": "https://api.gadgethumans.com/morse-code",
        "endpoint_path": "/morse-code",
        "content_intro": "The GadgetHumans Morse Code Converter API is a free REST API that converts between plain text and Morse code. Encode any text containing letters A-Z, numbers 0-9, and common punctuation into Morse code (dots and dashes), or decode Morse code sequences back into readable text. Perfect for educational apps, amateur radio tools, puzzles, cryptography lessons, and historical communication projects.",
        "content_detail": "Text-to-Morse conversion produces the standard International Morse Code representation with dots (.) and dashes (-), separated by spaces between letters and forward slashes (/) between words. Morse-to-text decoding accepts the same format. The free tier offers 100 requests per day with no API key required, making it ideal for learning platforms, STEM education tools, signal processing demonstrations, and hobbyist radio projects.",
        "features": [
            ("Text to Morse", "Convert alphanumeric text to International Morse Code (dots and dashes)."),
            ("Morse to Text", "Decode Morse code sequences back into readable text."),
            ("Standard Format", "Uses International Morse Code with space-separated letters and / for word separation."),
            ("Alphanumeric Support", "Supports A-Z, 0-9, and common punctuation characters."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What characters are supported?", "Letters A-Z, numbers 0-9, and common punctuation including period, comma, question mark, exclamation mark, and apostrophe."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("How are words separated in Morse code output?", "Words are separated by forward slash (/) between words, with letters within words separated by single spaces."),
            ("Can I decode Morse code without spaces?", "The decoder expects proper spacing between letters. Run-together Morse code may not decode accurately."),
            ("What Morse code standard is used?", "International Morse Code (ITU-R M.1677-1 standard)."),
        ],
        "related": [
            ("nato-phonetic", "🔊", "NATO Phonetic Alphabet", "Text to NATO alphabet"),
            ("case-converter", "🔤", "Text Case Converter", "UPPER, lower, Title, Sentence"),
            ("base64", "🔤", "Base64 Encode/Decode", "Encode & decode text"),
            ("roman-numerals", "🏛️", "Roman Numeral Converter", "Numbers to Roman numerals"),
        ],
        "curl_code": '# Encode text to Morse code\ncurl "https://api.gadgethumans.com/morse-code?text=SOS&mode=encode"\n\n# Decode Morse code to text\ncurl "https://api.gadgethumans.com/morse-code?text=...%20---%20...&mode=decode"',
        "python_code": 'import requests\n\n# Encode text to Morse code\nurl = "https://api.gadgethumans.com/morse-code"\nparams = {"text": "Hello World", "mode": "encode"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"Morse: {data["result"]}")',
        "js_code": '// Convert text to Morse code\nconst text = "SOS";\nfetch(`https://api.gadgethumans.com/morse-code?text=${encodeURIComponent(text)}&mode=encode`)\n  .then(res => res.json())\n  .then(data => {\n    console.log("Morse:", data.result);\n    document.getElementById("morseResult").textContent = data.result;\n  });',
    },
    {
        "path": "nato-phonetic",
        "emoji": "🔊",
        "title": "NATO Phonetic Alphabet API",
        "h1": "NATO Phonetic Alphabet API",
        "desc": "Free NATO Phonetic Alphabet API. Convert text to NATO phonetic alphabet words (Alpha, Bravo, Charlie...). REST API for radio communication, education, and spelling clarification.",
        "og_title": "NATO Phonetic Alphabet API — Free REST API",
        "og_desc": "Convert text to NATO phonetic alphabet words via REST API. Alpha, Bravo, Charlie — perfect for spelling clarification, radio, and education. Free tier, no signup.",
        "endpoint": "https://api.gadgethumans.com/nato-phonetic",
        "endpoint_path": "/nato-phonetic",
        "content_intro": "The GadgetHumans NATO Phonetic Alphabet API is a free REST API that converts text into NATO phonetic alphabet code words. Each letter is replaced with its internationally recognized code word: A becomes Alpha, B becomes Bravo, C becomes Charlie, and so on. Essential for spelling clarification in radio communications, customer service, education, and any situation where clear letter identification is critical.",
        "content_detail": "The API supports letters A-Z (both uppercase and lowercase), converts numbers 0-9 to their standard spoken forms, and passes through spaces and common punctuation. The output can be formatted as a list or a continuous string. The free tier offers 100 requests per day with no API key required, making it perfect for call center tools, aviation training apps, radio operator utilities, language learning platforms, and accessibility tools for spelling out names and addresses verbally.",
        "features": [
            ("Full NATO Standard", "Complete A-Z NATO phonetic alphabet: Alpha, Bravo, Charlie, Delta, etc."),
            ("Number Support", "Numbers 0-9 are converted to their standard spoken forms."),
            ("Flexible Output", "Choose between list format or continuous string output."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Edge-Deployed", "Cloudflare Workers with 320+ global edge locations for minimal latency."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What is the NATO phonetic alphabet?", "The NATO phonetic alphabet is a set of code words used to clearly identify letters in voice communication. For example, A=Alpha, B=Bravo, C=Charlie, etc."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("Are numbers supported?", "Yes, numbers 0-9 are converted to their standard spoken forms."),
            ("Can I use lowercase input?", "Yes, the API accepts both uppercase and lowercase letters."),
            ("How are spaces handled?", "Spaces are preserved in the output, allowing you to see word boundaries clearly."),
        ],
        "related": [
            ("morse-code", "📡", "Morse Code Converter", "Text to Morse code"),
            ("case-converter", "🔤", "Text Case Converter", "UPPER, lower, Title, Sentence"),
            ("base64", "🔤", "Base64 Encode/Decode", "Encode & decode text"),
            ("lorem-ipsum", "📄", "Lorem Ipsum Generator", "Placeholder text generation"),
        ],
        "curl_code": '# Convert text to NATO phonetic alphabet\ncurl "https://api.gadgethumans.com/nato-phonetic?text=HELLO"\n\n# Convert with numbers\ncurl "https://api.gadgethumans.com/nato-phonetic?text=SOS%201"',
        "python_code": 'import requests\n\n# Convert text to NATO phonetic alphabet\nurl = "https://api.gadgethumans.com/nato-phonetic"\nparams = {"text": "Hello World"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"Phonetic: {data["result"]}")',
        "js_code": '// Convert text to NATO phonetic alphabet\nconst text = "HELLO";\nfetch(`https://api.gadgethumans.com/nato-phonetic?text=${encodeURIComponent(text)}`)\n  .then(res => res.json())\n  .then(data => {\n    console.log("Phonetic:", data.result);\n    document.getElementById("natoResult").textContent = data.result;\n  });',
    },
    {
        "path": "random-generator",
        "emoji": "🎲",
        "title": "Random Number & Data Generator API",
        "h1": "Random Number & Data Generator API",
        "desc": "Free Random Number Generator API. Generate random integers, floats, dice rolls, lottery numbers, and more. REST API for games, simulations, and data sampling.",
        "og_title": "Random Generator API — Free Random Number & Data REST API",
        "og_desc": "Generate random numbers, dice rolls, and data via REST API. Min/max range, multiple values, and various data types. Free tier, no signup.",
        "endpoint": "https://api.gadgethumans.com/random",
        "endpoint_path": "/random",
        "content_intro": "The GadgetHumans Random Number & Data Generator API is a free REST API that generates cryptographically secure random numbers and data. Generate random integers within a range, floating-point numbers, simulate dice rolls, pick lottery numbers, shuffle lists, and more. Perfect for game development, statistical sampling, simulations, testing, and any application that needs unbiased random data.",
        "content_detail": "Specify the type of random data you need: integers between min and max values, floating-point numbers, dice rolls (1d6, 2d20, etc.), lottery-style number picks without replacement, or random boolean values. Control how many results to generate in a single request. Uses cryptographically secure random number generation for true unpredictability. The free tier offers 100 requests per day with no API key required, making it ideal for game developers, data scientists, educators building probability demonstrations, and developers needing test data generation.",
        "features": [
            ("Multiple Data Types", "Integers, floats, dice rolls, lottery picks, booleans, and list shuffles."),
            ("Configurable Range", "Set minimum and maximum values for random number generation."),
            ("Dice Roll Simulator", "Simulate any dice: 1d6, 2d20, 3d10, etc. Returns individual rolls and totals."),
            ("Cryptographically Secure", "Uses secure random generation — truly unpredictable results."),
            ("100% Free Tier", "No API key, no signup, no credit card. 100 requests per day included."),
            ("Pro Tier", "$5/month unlocks 10,000 requests/day with dedicated API key."),
        ],
        "faq": [
            ("What types of random data can I generate?", "Integers, floating-point numbers, dice rolls, lottery picks (without replacement), booleans, and list shuffles."),
            ("Do I need an API key?", "No! The free tier requires no API key or signup."),
            ("Are the numbers truly random?", "Yes, the API uses cryptographically secure pseudo-random number generation (CSPRNG)."),
            ("Can I roll multiple dice at once?", "Yes! Use dice notation like '2d20' to roll two 20-sided dice. The API returns individual rolls and the total."),
            ("What is lottery mode?", "Lottery mode picks N numbers from a range without replacement — like drawing lottery balls from a drum."),
        ],
        "related": [
            ("password", "🔐", "Secure Password Generator", "Generate secure random passwords"),
            ("uuid", "🎲", "UUID Generator", "v4 unique identifiers"),
            ("lorem-ipsum", "📄", "Lorem Ipsum Generator", "Placeholder text generation"),
            ("dice-roller", "🎲", "Dice Roller", "Virtual dice rolling"),
        ],
        "curl_code": '# Generate a random integer between 1 and 100\ncurl "https://api.gadgethumans.com/random?type=integer&min=1&max=100&count=1"\n\n# Roll 2 six-sided dice\ncurl "https://api.gadgethumans.com/random?type=dice&dice=2d6"\n\n# Pick 6 lottery numbers from 1-49\ncurl "https://api.gadgethumans.com/random?type=lottery&min=1&max=49&count=6"',
        "python_code": 'import requests\n\n# Generate random numbers\nurl = "https://api.gadgethumans.com/random"\n\n# Random integer\nparams = {"type": "integer", "min": 1, "max": 100, "count": 5}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"Random numbers: {data["numbers"]}")\n\n# Roll dice\nparams = {"type": "dice", "dice": "2d6"}\nresponse = requests.get(url, params=params)\ndata = response.json()\nprint(f"Dice roll: {data["result"]}")',
        "js_code": '// Get random numbers from the browser\nfetch("https://api.gadgethumans.com/random?type=integer&min=1&max=100&count=5")\n  .then(res => res.json())\n  .then(data => {\n    console.log("Random numbers:", data.numbers);\n    document.getElementById("randomResult").textContent = \n      data.numbers.join(", ");\n  });',
    },
]


def generate_page(tool):
    path = tool["path"]
    title = tool["title"]
    h1_emoji = tool["emoji"]
    h1 = tool["h1"]
    desc = tool["desc"]
    og_title = tool["og_title"]
    og_desc = tool["og_desc"]
    endpoint = tool["endpoint"]
    endpoint_path = tool["endpoint_path"]
    intro = tool["content_intro"]
    detail = tool["content_detail"]
    features = tool["features"]
    faq = tool["faq"]
    related = tool["related"]
    curl_code = tool["curl_code"]
    python_code = tool["python_code"]
    js_code = tool["js_code"]
    
    canonical = f"https://www.gadgethumans.com/tools/{path}/"
    og_url = canonical
    
    # Build features HTML
    features_html = ""
    for icon, text in features:
        features_html += f'      <li><strong>✅ {icon}</strong> — {text}</li>\n'
    
    # Build FAQ HTML
    faq_html = ""
    for q, a in faq:
        faq_html += f'''    <div class="faq-item">
      <h4>{q}</h4>
      <p>{a}</p>
    </div>
'''
    
    # Build related links HTML
    related_html = ""
    for r_path, r_emoji, r_name, r_desc in related:
        related_html += f'''      <a href="/tools/{r_path}/" class="related-card">
        <span class="emoji">{r_emoji}</span>
        <span class="name">{r_name}</span>
        <span class="desc">{r_desc}</span>
      </a>
'''
    
    # Internal nav links
    nav_links = """      <a href="/">Home</a>
      <a href="/tools/" class="active">Tools</a>
      <a href="/bluetooth-speakers/reviews/">Reviews</a>
      <a href="/bluetooth-speakers/guides/">Guides</a>
      <a href="/bluetooth-speakers/blog/">Blog</a>"""
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="google-site-verification" content="UDV2Y8alLItYNDuunh6l8XiwbiljzzxK-UGWnWY6biA" />
  <title>{title} | GadgetHumans</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{', '.join([r_name.lower() for r_name in [title]] + [path.replace('-', ' ') + ' api', 'free ' + path.replace('-', ' ') + ' api', path.replace('-', ' ') + ' rest api'])}">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{og_desc}">
  <meta property="og:url" content="{og_url}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://www.gadgethumans.com/images/og-tools.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="{CSS_PATH}">
  <script src="{JS_PATH}" defer></script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebAPI",
    "name": "{title}",
    "description": "{desc}",
    "url": "{canonical}",
    "provider": {{
      "@type": "Organization",
      "name": "GadgetHumans",
      "url": "https://www.gadgethumans.com"
    }},
    "documentation": "{endpoint}/",
    "endpoint": "{endpoint}"
  }}
  </script>
  <style>
    .breadcrumb {{ font-size: 0.82rem; color: var(--muted); margin: 20px 0 8px; display: flex; gap: 6px; flex-wrap: wrap; }}
    .breadcrumb a {{ color: var(--accent); text-decoration: none; }}
    .breadcrumb a:hover {{ text-decoration: underline; }}
    .breadcrumb span {{ color: var(--muted); }}
    .tool-hero {{ text-align: center; padding: 40px 0 24px; }}
    .tool-hero h1 {{ font-family: var(--font-display); font-size: 2.4rem; font-weight: 800; letter-spacing: -0.03em; margin-bottom: 12px; }}
    .tool-hero p {{ font-size: 1.05rem; color: var(--text2); max-width: 640px; margin: 0 auto 8px; line-height: 1.6; }}
    .tool-hero .endpoint-badge {{ display: inline-block; font-family: var(--mono); font-size: 0.85rem; background: var(--accent-dim); color: var(--accent); padding: 6px 16px; border-radius: 980px; margin-top: 8px; }}
    .section {{ margin: 40px 0; }}
    .section h2 {{ font-family: var(--font-display); font-size: 1.5rem; font-weight: 700; margin-bottom: 16px; letter-spacing: -0.02em; }}
    .section h3 {{ font-size: 1.1rem; font-weight: 600; margin: 20px 0 8px; }}
    .section p, .section li {{ color: var(--text2); line-height: 1.7; font-size: 0.95rem; }}
    .section ul {{ padding-left: 20px; margin: 12px 0; }}
    .section ul li {{ margin-bottom: 6px; }}
    .code-block {{ background: #1a1a2e; color: #e4e4e4; padding: 16px 20px; border-radius: var(--radius); overflow-x: auto; font-family: var(--mono); font-size: 0.82rem; line-height: 1.6; margin: 12px 0; }}
    .code-block .comment {{ color: #6a9955; }}
    .code-block .keyword {{ color: #569cd6; }}
    .code-block .string {{ color: #ce9178; }}
    .code-block .function {{ color: #dcdcaa; }}
    .try-card {{ background: var(--glass-bg); backdrop-filter: blur(var(--glass-blur-sm)); -webkit-backdrop-filter: blur(var(--glass-blur-sm)); border: 1px solid var(--glass-border); border-radius: var(--radius-lg); padding: 28px; margin: 24px 0; }}
    .try-card h3 {{ margin-bottom: 16px; }}
    .try-card label {{ display: block; font-size: 0.85rem; font-weight: 600; color: var(--text2); margin-bottom: 6px; }}
    .try-card input, .try-card select {{ width: 100%; padding: 10px 14px; background: var(--bg); border: 1px solid var(--border); border-radius: var(--radius); font-family: var(--font); font-size: 0.9rem; color: var(--text); outline: none; margin-bottom: 14px; }}
    .try-card input:focus, .try-card select:focus {{ border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-dim); }}
    .try-card .btn {{ padding: 10px 24px; background: var(--accent); color: #fff; border: none; border-radius: 980px; font-size: 0.9rem; font-weight: 600; cursor: pointer; transition: all 0.2s; }}
    .try-card .btn:hover {{ background: var(--accent-hover); transform: translateY(-1px); }}
    .try-card .result {{ margin-top: 16px; padding: 16px; background: var(--bg); border-radius: var(--radius); border: 1px solid var(--border); min-height: 80px; word-break: break-all; font-family: var(--mono); font-size: 0.82rem; }}
    .faq-item {{ margin-bottom: 16px; }}
    .faq-item h4 {{ font-size: 1rem; font-weight: 600; margin-bottom: 4px; cursor: pointer; }}
    .faq-item h4:hover {{ color: var(--accent); }}
    .faq-item p {{ font-size: 0.9rem; color: var(--text2); }}
    .related-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; margin-top: 16px; }}
    .related-card {{ display: flex; flex-direction: column; align-items: center; text-align: center; padding: 20px 12px; background: var(--glass-bg); backdrop-filter: blur(var(--glass-blur-sm)); -webkit-backdrop-filter: blur(var(--glass-blur-sm)); border: 1px solid var(--glass-border); border-radius: var(--radius-lg); text-decoration: none; color: inherit; transition: all 0.2s; gap: 6px; }}
    .related-card:hover {{ border-color: var(--accent); transform: translateY(-3px); box-shadow: var(--glass-shadow-hover); }}
    .related-card .emoji {{ font-size: 1.8rem; }}
    .related-card .name {{ font-size: 0.85rem; font-weight: 600; }}
    .related-card .desc {{ font-size: 0.72rem; color: var(--muted); }}
    @media (max-width: 480px) {{ .tool-hero h1 {{ font-size: 1.6rem; }} .related-grid {{ grid-template-columns: 1fr 1fr; }} }}
  </style>
</head>
<body>
<nav>
  <div class="nav-inner">
    <a href="/" class="nav-logo">GadgetHumans</a>
    <button class="nav-toggle" aria-label="Menu">☰</button>
    <div class="nav-links">
{nav_links}
    </div>
  </div>
</nav>
<div class="container">
  <!-- Breadcrumb -->
  <div class="breadcrumb">
    <a href="/">Home</a> › <a href="/tools/">Tools</a> › <span>{h1}</span>
  </div>

  <!-- Hero -->
  <div class="tool-hero">
    <h1>{h1_emoji} {h1}</h1>
    <p>{desc}</p>
    <span class="endpoint-badge">GET {endpoint}?...</span>
  </div>

  <!-- API Services Banner -->
  <div class="api-banner" style="margin: 24px 0; padding: 20px 24px; background: linear-gradient(135deg, rgba(96,165,250,0.08), rgba(167,139,250,0.08)); border: 1px solid rgba(96,165,250,0.2); border-radius: 16px; display: flex; flex-wrap: wrap; gap: 12px; align-items: center; justify-content: center;">
    <span style="font-size: 1.1rem; font-weight: 700;">⚡ API Hub — All Endpoints</span>
    <a href="https://api.gadgethumans.com/" target="_blank" rel="noopener" style="padding: 6px 16px; background: #60a5fa; color: #fff; border-radius: 980px; text-decoration: none; font-size: 0.8rem; font-weight: 600;">📱 API Hub Overview</a>
    <a href="{endpoint}/" target="_blank" rel="noopener" style="padding: 6px 16px; background: #a78bfa; color: #fff; border-radius: 980px; text-decoration: none; font-size: 0.8rem; font-weight: 600;">📖 API Docs</a>
  </div>

  <!-- Description Section -->
  <div class="section">
    <h2>What is the {h1}?</h2>
    <p>{intro}</p>
    <p>{detail}</p>
  </div>

  <!-- Quick Start Code Examples -->
  <div class="section">
    <h2>⚡ Quick Start</h2>
    <p>Get started with a simple GET request. No authentication required.</p>

    <h3>cURL</h3>
    <div class="code-block">
      <span class="comment"># Quick example</span><br>
      {curl_code.replace(chr(10), '<br>      ')}
    </div>

    <h3>Python</h3>
    <div class="code-block">
      {python_code.replace(chr(10), '<br>      ')}
    </div>

    <h3>JavaScript (Fetch)</h3>
    <div class="code-block">
      {js_code.replace(chr(10), '<br>      ')}
    </div>
  </div>

  <!-- Features / Benefits -->
  <div class="section">
    <h2>✨ Features &amp; Benefits</h2>
    <ul>
{features_html}
    </ul>
  </div>

  <!-- FAQ Section -->
  <div class="section">
    <h2>❓ Frequently Asked Questions</h2>
{faq_html}
  </div>

  <!-- Internal Links -->
  <div class="section">
    <h2>🔗 Related Tools &amp; APIs</h2>
    <div class="related-grid">
{related_html}
      <a href="https://api.gadgethumans.com/" target="_blank" rel="noopener" class="related-card">
        <span class="emoji">⚡</span>
        <span class="name">API Hub</span>
        <span class="desc">All free APIs</span>
      </a>
    </div>
  </div>

  <footer>
    <div class="footer-links">
      <a href="/">Home</a>
      <a href="/tools/">Tools</a>
      <a href="/bluetooth-speakers/reviews/">Reviews</a>
      <a href="/bluetooth-speakers/guides/">Buying Guides</a>
      <a href="/bluetooth-speakers/blog/">Blog</a>
      <a href="https://payhip.com/b/fdwTJ">✨ Free</a><a href="https://payhip.com/b/Vu3q0" class="nav-cta-mid">📋 Pro €7</a><a href="https://payhip.com/b/9x3Ee" class="nav-cta-pro">🚀 Launch €17</a>
      <a href="/privacy/">Privacy</a>
    </div>
    <p>© 2026 <a href="https://www.gadgethumans.com">GadgetHumans</a> — Tech reviews, deals &amp; AI tools</p>
    <p class="affiliate-disclosure">As an Amazon Associate, GadgetHumans earns from qualifying purchases.</p>
  </footer>
</div>

<script src="{SCRIPT_JS}"></script>
<!-- Premium Upsell CTA -->
<div class="card" style="max-width: 620px; margin: 40px auto 24px; text-align: center;">
  <div style="position: relative; z-index: 1;">
    <h3 style="margin: 0 0 12px; font-size: 1.15rem; font-weight: 700; color: var(--text);">🚀 Need more power?</h3>
    <p style="margin: 0 0 18px; font-size: 0.85rem; color: var(--text2); line-height: 1.5;">
      Get the <strong>AI Agent Launch Plan</strong> with 50+ pro prompts
    </p>
    <div style="display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;">
      <a href="https://payhip.com/b/9x3Ee" target="_blank" rel="noopener" style="display: inline-flex; align-items: center; gap: 6px; padding: 11px 24px; background: linear-gradient(135deg, #007AFF, #5856D6); color: #fff; border: none; border-radius: 980px; font-size: 0.85rem; font-weight: 600; text-decoration: none; transition: all 0.25s ease; box-shadow: 0 4px 14px rgba(0, 122, 255, 0.35);">🚀 AI Agent Launch Plan — €17</a>
      <a href="https://payhip.com/b/Vu3q0" target="_blank" rel="noopener" style="display: inline-flex; align-items: center; gap: 6px; padding: 11px 24px; background: var(--glass-bg); backdrop-filter: blur(var(--glass-blur-sm)); -webkit-backdrop-filter: blur(var(--glass-blur-sm)); border: 1px solid var(--glass-border); color: var(--text); border-radius: 980px; font-size: 0.85rem; font-weight: 600; text-decoration: none; transition: all 0.25s ease;">📋 Implementation Checklist — €7</a>
    </div>
  </div>
</div>
</body>
</html>'''

def main():
    for tool in TOOLS:
        path = tool["path"]
        dir_path = os.path.join(BASE, "tools", path)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, "index.html")
        html = generate_page(tool)
        with open(file_path, "w") as f:
            f.write(html)
        print(f"✓ Created {file_path}")

if __name__ == "__main__":
    main()
