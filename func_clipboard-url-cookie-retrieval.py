import pyperclip
import re
from http import cookies


def extract_cookies_from_clipboard():
    clipboard_content = pyperclip.paste()

    cookie_pattern = r"Set-Cookie: ([^;]+)"
    matches = re.findall(cookie_pattern, clipboard_content, re.IGNORECASE)

    if matches:
        cookie_jar = cookies.SimpleCookie()
        for match in matches:
            cookie_jar.load(match)
        return cookie_jar
    else:
        print("No cookies found in clipboard content.")
        return None


if __name__ == "__main__":
    cookie_jar = extract_cookies_from_clipboard()

    if cookie_jar:
        for key, morsel in cookie_jar.items():
            print(f"{key}: {morsel.value}")
