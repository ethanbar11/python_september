# import string
#
#
# def get_ceaser_next(c, num):
#     abc = string.ascii_lowercase
#     index = abc.index(c)
#     index_new = (index + num) % len(abc)
#     return abc[index_new]
#
#
# def encrypt(msg, num):
#     msg = msg.lower()
#     abc = string.ascii_lowercase
#     new_msg = ''
#     for c in msg:
#         if c in abc:
#             new_msg = new_msg + get_ceaser_next(c, num)
#         else:
#             new_msg = new_msg + c
#     return new_msg
#
#
# def decrypt(msg, num):
#     return encrypt(msg, -num)
#
#
# if __name__ == '__main__':
#     path = 'fi.txt'
#     import json
#
#     with open(path, 'r') as fi:
#         msg = fi.read()
#         json.dump({'Hello': 'Hello'}, fi)
#     with open(path, 'w') as fi:
#         new_msg = encrypt(msg, num=2)
#         fi.write(new_msg)
# # if __name__ == '__main__':
# #     msg='abc!1234'
# #     encrypted_msg=encrypt(msg,2)
# #     print(encrypted_msg)
# #     print(decrypt(encrypted_msg,2))
