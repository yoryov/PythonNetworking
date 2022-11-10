import urllib.request

print("Downloading...")
url="https://www.python.org/static/img/python-logo.png"
urllib.request.urlretrieve(url,"image.png") # download python