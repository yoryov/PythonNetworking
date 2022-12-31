import shodan
import re
import os

# Remember to store securely your SHODAN API Key

SHODAN_KEY = os.environ['shodanapikey']
recon = shodan.Shodan(SHODAN_KEY)

ftp_servers = []

try:
    shodan_search = recon.search("port: 21 Anonymous user logged in") # Searching for open FTP servers wihtout username or password
    print("Hosts: ", str(len(shodan_search['matches'])))
    for result in shodan_search['matches']:
        if result['ip_str'] is not None:
            ftp_servers.append(result['ip_str'])

    for server in ftp_servers:
        print(server)
except shodan.APIError as e:
    print(str(e))
