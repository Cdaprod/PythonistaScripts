import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import clipboard

def modify_url_params(url, params_to_modify):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    for key, value in params_to_modify.items():
        query_params[key] = value

    modified_query = urlencode(query_params, doseq=True)
    modified_url = urlunparse(parsed_url._replace(query=modified_query))
    return modified_url

# Get URL from clipboard
url = clipboard.get()

# Define the parameters to modify
params_to_modify = {
    "param1": "new_value1",
    "param2": "new_value2"
}

# Modify URL parameters
modified_url = modify_url_params(url, params_to_modify)

# Print the modified URL
print(modified_url)

# Copy the modified URL to clipboard
clipboard.set(modified_url)
