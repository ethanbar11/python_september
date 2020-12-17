import requests

# r = requests.get('http://127.0.0.1:5000/hello')
# print(r.content.decode())

r2=requests.get('http://127.0.0.1:5000/bla_bla/EthanBar')
print(r2.content.decode())