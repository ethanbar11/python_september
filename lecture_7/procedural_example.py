x = 5


def func2(y):
    return y + 10


def func(y):
    return y + func2(y) + 5


print(func(x))
