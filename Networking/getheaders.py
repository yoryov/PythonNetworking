import urllib.request
from urllib.request import Request

target="https://linux.org"

USER_AGENT = "Mozilla/4.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36"

def firefox_user_agent():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', USER_AGENT)]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(target)
