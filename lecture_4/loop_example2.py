# len(lst1)==len(lst2), no recurring items in the lists.
def has_the_same_things(lst1, lst2):
    counter = 0
    for elem in lst1:
        for elem2 in lst2:
            if elem == elem2:
                counter += 1
    if counter == len(lst1):
        return True
    return False


def has_the_same_things2(lst1, lst2):
    for elem in lst1:
        has_found_elem = False
        for elem2 in lst2:
            if elem == elem2:
                has_found_elem = True
        if has_found_elem == False:
            return False
    return True


x = [5, 'Hello', True]

y = ['Hello', 5, True]
z = [4, 2, 1]
print(has_the_same_things(x, y))
