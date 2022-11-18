import requests

def torconnection():
    session = requests.session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    return session

session = torconnection()
print("Tor IP:", session.get("https://httpbin.org/ip").text)
try:
    response = session.get('http://ciadotgov4sjwlzihbbgxnqg3xiyrgso2r2o3lt5wz5ypk4sxyjstad.onion/')
    for key,value in response.headers.items():
        #if key == 'Server':
            print(key,value)
except Exception as e:
    print("An error ocurred :( \n" + str(e))
