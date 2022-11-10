import requests
import re

url = "https://www.python.org"
var = requests.get(url).text

for link,name in re.findall("<a (.*)>(.*)</a>",var):
    for a in link.split():
        if re.findall("href=(.*)",a):
            url_image = a[0:-1].replace("href=\"","")
            if(url_image.startswith("http")):
                print(url_image)
            else:
                print(url+url_image)
