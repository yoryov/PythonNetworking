# Make sure to control your credits at https://developer.shodan.io/dashboard :p

import shodan
import os
import sys
import argparse
import socket

SHODAN_KEY = os.environ['shodanapikey']
recon = shodan.Shodan(SHODAN_KEY)

parser = argparse.ArgumentParser(description='Shodan API Search!')

# adding 2 arguments

parser.add_argument("--target", "-t", dest="target", help="Target IP or Domain",required=None)
parser.add_argument("--search", "-s", dest="search", help="Normal Shodan Search", required=None)
parsed_args = parser.parse_args() # Parsing the arguments


if sys.argv[1] == '--search' or '-s':
    try:
        results = recon.search(parsed_args.search)
        print('Results: %s' %results['total'])
        for result in results['matches']:
            print('IP: %s' %result['ip_str'])
            print(result['data'])
    except shodan.APIError as e:
        print(str(e))

if sys.argv[1] == '--target' or '-t':
    try:
        hostname = socket.gethostbyname(parsed_args.target)
        results = recon.host(hostname)
        print("""IP: %s \nOrganization: %s \nOS: %s """ 
        % (results['ip_str'], results.get('org','n/a'), results.get('os', 'n/a')))
        for item in results['data']:
            print("""Port: %s \nBanner: %s """ 
            % (item['port'], item['data']))
    except shodan.APIError as e:
        print(str(e))

