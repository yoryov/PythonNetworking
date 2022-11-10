import requests
import re

url = input("URL: ")
var = requests.get(url).text
print("Links: ")
print("###############")
for link in re.findall("<a (.*)></a>",var):
    for a in link.split():
        if re.findall("href=(.*)",a):
            url_link = a[0:-1].replace("href=","")
            if(url_link.startswith("http")):
                print(url_link)
            else:
                print(url+url_link)