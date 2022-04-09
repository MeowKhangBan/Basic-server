from encodings import utf_8
import socket
serverip = 'localhost'
port = 7000

while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    server.bind((serverip,port))
    server.listen(5)
    print('Waiting for client...')

    client,addr = server.accept()
    print('Server connect from :',str(addr))
    data = client.recv(1024).decode('utf_8')
    print('Message from client:',data)
    client.send('We receive your message'.encode('utf_8'))
    client.close()    
