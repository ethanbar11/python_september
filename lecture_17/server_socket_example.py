import socket

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Starting server socket with port {}'.format(15000))
# bind the socket to a public host, and a well-known port
serversocket.bind(('127.0.0.1', 15000))
# become a server socket
serversocket.listen(5)
print('Starting to listen')
(clientsocket, address) = serversocket.accept()
print('Accepted client')
while True:
    msg = clientsocket.recv(1024)
    if msg == b'':
        break
    else:
        print('got message : ' + msg.decode())
        clientsocket.send(b'This is server sending message to client!')
