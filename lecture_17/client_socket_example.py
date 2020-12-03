import socket

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 15000 - the normal http port
s.connect(("127.0.0.1", 15000))
s.send(b'Hello There!')
s.close()
