import urllib.request
from urllib.request import Request

target="https://python.org"

USER_AGENT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

def firefox_user_agent():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', USER_AGENT)]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(target)
    print("Server Information: ")
    print("----------------------")
    for header, value in response.getheaders():
        #if header == ("Server" or "server"): # With this If statement we can get only the web server
            print(header + ":" + value)
    
    request = Request(target)
    request.add_header('User-agent', USER_AGENT)
    print("\nRequest headers")
    print("----------------------")
    for header, value in request.header_items():
        print(header + ":" + value)

if __name__ == '__main__':
    firefox_user_agent()
