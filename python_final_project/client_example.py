import requests

# r = requests.get('http://127.0.0.1:5000/hello')
# print(r.content.decode())
s=requests.Session()
response_from_server = s.get('http://127.0.0.1:5000/login/ethan/bar')
print(response_from_server.content.decode())
# Sending post requests

response_from_server = s.get('http://127.0.0.1:5000/logout')
print(response_from_server.content.decode())
