import urllib.request

print("Downloading...")
url="https://www.python.org/static/img/python-logo.png"
filename = "python-logo.png"

with urllib.request.urlopen(url) as response:
    print(response.status)
    with open(filename, "wb") as image:
        image.write(response.read())