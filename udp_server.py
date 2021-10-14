# UDP/IP

# import socket -> #socket.socket
from socket import *

serverPort = 30000
# SOCK_STREAM -> 연결된 상태에서 데이터를 보냄 SOCK_DGRAM -> 연결없이 데이터를 보냄
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind("0.0.0.0", 30000)
print("서버에서 수신할 준비가 완료되었습니다.")

try:
    while True:
        m, a = serverSocket.recvfrom(8192)
        print("{}".format(m.decode()))
except KeyboardInterrupt:
    serverSocket.close()
