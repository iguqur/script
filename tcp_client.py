import socket

HOST = '192.168.71.115'    # The remote host
PORT = 5003             # The same port as used by the server

sendDataStr = '68 05 00 00 04 06 11 01 89 FE'



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    i = 0;
    # while True:

    s.sendall(bytes.fromhex(sendDataStr))
    data = s.recv(1024)

    # print(type(data))
    i = i+1
    print('Received:', data.hex(), 'i: ', i)

