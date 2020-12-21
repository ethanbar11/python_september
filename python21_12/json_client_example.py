import requests

respon = requests.post('http://127.0.0.1:5000/validate_snake', json={'snake2': 'Bla'})
print(respon.content.decode())
