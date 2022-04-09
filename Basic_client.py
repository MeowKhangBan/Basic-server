import socket
serverip = 'localhost'
port = 7000

while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.connect((serverip,port))
    data = input('Message : ')
    server.send(data.encode('utf-8'))

    data_server = server.recv(1024).decode('utf-8')
    print('From servers : ',data_server)
    server.close()