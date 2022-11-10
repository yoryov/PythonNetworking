import requests
import re

url = "https://www.python.org"
var = requests.get(url).text
#print(var)
for link in re.findall("<a href=\"https://(.*).python.org\">",var):
    print(link)
"""

    for a in link.split():
        if re.findall("href=(.*)",a):
            url_link = a[0:-1].replace("href=\"","")
            if(a.startswith("http")):
                print(a)
            else:
                print(url+url_link)
"""
