def get_one_integer():
    try:
        x = int(input('Please enter number'))
        if x < 0 or x > 10000:
            return None
        return x
    except:
        return None


def get_integer():
    x = get_one_integer()
    while x == None:
        x = get_one_integer()
    return x

print(get_integer())