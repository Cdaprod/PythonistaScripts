import pyperclip
import requests

def get_response_headers_from_clipboard_url():
    url = pyperclip.paste()
    
    try:
        response = requests.get(url)
        headers = response.headers
        return headers
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    headers = get_response_headers_from_clipboard_url()

    if headers:
        for key, value in headers.items():
            print(f"{key}: {value}")
