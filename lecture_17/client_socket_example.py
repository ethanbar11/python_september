import socket

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Created client')
# now connect to the web server on port 15000 - the normal http port
s.connect(("127.0.0.1", 15000))
print('Connected to 127.0.0.1 in port 15000')
msg = s.recv(1024)
print('Got message from server :{} '.format(msg.decode()))
msg_to_send = input('What to send? : ').encode()
s.send(msg_to_send)
msg = s.recv(1024)
print('Got message from server : {}'.format(msg.decode()))
s.close()
print('Closing')
