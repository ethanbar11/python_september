def a():
    return 4 / 0


def b():
    return a()


# try:

print(b())
# except:
#     print('There was an exception at b!')
