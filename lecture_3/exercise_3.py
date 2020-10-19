a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# length_of_a = len(a)
# for i in range(length_of_a):
#     if a[i] < 5:
#         print(a[i])

# second
# smaller_than_5=[]
# for i in range(len(a)):
#     if a[i]<5:
#         smaller_than_5.append(a[i])
# print(smaller_than_5)

# third
# def print_if_smaller_than_5(x):
#     if x<5:
#         print(x)
# list(map(print_if_smaller_than_5,a ))
y=[print(x) for x in a if x<5]