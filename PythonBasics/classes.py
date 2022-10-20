class protocol(object):
    def __init__(self, name, port, description):
        self.name = name
        self.port = port
        self.description = description
    def getProtocolInfo(self):
        return self.name+" "+str(self.port)+" "+self.description

protocol_http = protocol("HTTP", 80, "Hypertext Transfer Protocol")
print(protocol_http.name, protocol_http.port)
print(protocol_http.getProtocolInfo())


class mylist(protocol):
    def max_min(self):
        return max(self), min(self)

list1 = mylist("HTTPS", 443, "Hypertext Transfer Protocol Secure")
print(list1.max_min(80,50,40))