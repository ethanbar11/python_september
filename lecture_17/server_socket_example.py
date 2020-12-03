import socket

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind(('127.0.0.1', 15000))
# become a server socket
serversocket.listen(5)
(clientsocket, address) = serversocket.accept()
while True:
    msg = clientsocket.recv(1024)
    if msg == b'':
        break
    else:
        print(msg.decode())
