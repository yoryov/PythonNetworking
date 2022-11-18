# Remember to start a Tor connection, port 9050 with the SOCKS protocol, 
# If you have WSL is possible to install tor and set up a Tor connection through there 

import requests

tor_sites = ['http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/',
            'http://s4k4ceiapwwgcm3mkb6e4diqecpo7kvdnfr5gg7sph7jjppqkvwwqtyd.onion/',
            'http://6nhmgdpnyoljh5uzr5kwlatx2u3diou4ldeommfxjz3wkhalzgjqxzqd.onion/',
            'http://6nhmgdpnyoljh5uzr5kwlatx2u3diou4ldeommfxjz3wkhalzgjqxzqd.onion/',
            'http://jgwe5cjqdbyvudjqskaajbfibfewew4pndx52dye7ug3mt3jimmktkid.onion/'
]

def torconnection():
    session = requests.session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    return session

session = torconnection()
print("Tor IP:", session.get("https://ipecho.net/plain").text)
for torsite in tor_sites:
    try:
        response = session.get(torsite)
        for key,value in response.headers.items():
            if key == 'Server':
                print("[*]",key,value)
    except Exception as e:
        print("[-]An Error ocurred \n" + str(e))

