# for i in range(1, 10000):
#     print(i)
#     if i == 1000:
#         break
def add_one(num):
    x = num + 1
    return x


def is_lists_equals(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True


x = [1, 2, 3]
y = [3, 1, 2]
print(is_lists_equals(x, x))
# a = 2
# y = add_one(a)
# a = a + 1
# print(y)

b = 2
b = b + 1
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum_of_lst = sum(lst)
# print(sum_of_lst)
