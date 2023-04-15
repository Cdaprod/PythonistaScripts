import requests
import shutil

def install_requests():
    url = "https://github.com/psf/requests/archive/refs/tags/v2.26.0.zip"
    response = requests.get(url, stream=True)
    with open("requests.zip", "wb") as out_file:
        shutil.copyfileobj(response.raw, out_file)
    import zipfile
    with zipfile.ZipFile("requests.zip", "r") as zip_ref:
        zip_ref.extractall()

install_requests()
