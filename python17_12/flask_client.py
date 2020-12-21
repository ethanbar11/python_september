import requests

# r = requests.get('http://127.0.0.1:5000/hello')
# print(r.content.decode())

response_from_server = requests.get('http://127.0.0.1:5000/')
print(response_from_server.content.decode())
# Sending post requests
respon = requests.post('http://127.0.0.1:5000/')
