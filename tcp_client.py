import socket

HOST = '192.168.83.24'    # The remote host
PORT = 5003             # The same port as used by the server

sendDataStr = '22 33'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes.fromhex(sendDataStr))
    data = s.recv(1024)

print(type(data))
print('Received:', data.hex())
