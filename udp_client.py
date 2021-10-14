from socket import *

host = "slogs.dev"
port = 30001

c = socket(AF_INET, SOCK_DGRAM)
msg = "^_^"
c.sendto(msg.encode(), (host, port))
c.close()
