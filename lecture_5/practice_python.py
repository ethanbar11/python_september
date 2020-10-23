import string
import random

letters = string.punctuation + string.ascii_letters + string.digits
PASSWORD_LENGTH = 16
password = ''
for i in range(PASSWORD_LENGTH):
    rand = random.randint(0, len(letters) - 1)
    password += letters[rand]
print(password)