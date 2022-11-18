import http.client

connection = http.client.HTTPConnection("blog.cyberoperator.dev")
connection.request("GET","/")
response = connection.getresponse()
print(response.status, response.reason)
print(response.read())