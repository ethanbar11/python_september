import math


def special_sum(a, b):
    return a * 5 + b / 3 + 2


# a>0
# When the operation of the function is invalid, returns -1.
def get_number_plus_2(a):
    if math.isnan(a):
        return -1
    return a + 2


num1 = 5
num2 = 3
if num1 == num2:
    print('hello')
lst = [1, 2, 3]
print(lst[5])
# print(special_sum('Hello', 5))
x = input('please enter number >0')
while get_number_plus_2(x) == -1:
    x = input('please enter number > 0')
print(x)
