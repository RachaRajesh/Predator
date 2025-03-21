# Predator - Lightweight Web App Fuzzer

Predator is a simple proof-of-concept web application fuzzer designed to detect common vulnerabilities like SQL Injection and Cross-Site Scripting (XSS) in PHP-based web applications.

## Features
- Sends crafted inputs to web forms using POST requests
- Detects SQLi/XSS via response analysis
- Logs vulnerable inputs and highlights potential attacks

## Getting Started

### Requirements
- Python 3.x
- `requests` library
- A local web server (e.g., XAMPP, WAMP) running a PHP app

### Installation
```bash
pip install -r requirements.txt
```

### Usage
1. Place `vulnerable_app.php` in your web server directory (e.g., htdocs).
2. Update `TARGET_URL` in `predator_fuzzer.py` to match your local server URL.
3. Run the fuzzer:
```bash
python predator_fuzzer.py
```

