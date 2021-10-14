import socket

# 서버 코드

# AF_INET, SOCK_STREAM -> TCP/IP 설정
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 127.0.0.1 = localhost, 내부에서 접근 O / 외부에서 접근 X
# 테스트를 위한 용도 또는 내부 서비스 활용 용도
# 0.0.0.0:30000 = 외부에서 접근 가능한 IP (247.82.29.50:30000)
# *방화벽에서 포트는 개방되어 있어야 함.

s.bind(('0.0.0.0', 30000))
s.listen(0)
c, addr = s.accept()
print('{}, {}'.format(c, addr))

data = c.recv(1024)
print('받은 데이터 : {}'.format(data.decode()))

c.close()
s.close()
