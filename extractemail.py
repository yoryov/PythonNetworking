import urllib.request
import re

USER_AGENT = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
target = "https://example.com"
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent',USER_AGENT)]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(target)
html_content = response.read()
repattern = re.compile( r"[-a-zA-Z0-9._]+[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
mails = re.findall(repattern,str(html_content))
print(mails)
