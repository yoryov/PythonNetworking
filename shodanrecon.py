import shodan
import os

SHODAN_KEY = os.environ['shodanapikey']
recon = shodan.Shodan(SHODAN_KEY)

try:
    result = recon.search('Apache')
    print('results:',result.items())
except Exception as e:
    print(str(e))