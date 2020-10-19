amount = int(input("Please enter fibonnaci numbers amount"))
# first = 1
# second = 1
# print(first)
# print(second)
# for i in range(2, amount):
#     # Summing first and second.
#     the_new_sum = first + second
#     # Printing the next number
#     print(the_new_sum)
#     #
#     first = second
#     second = first + second

# Second way
fib = [1, 1]
for i in range(2, amount):
    sum_of_numbers = fib[i - 2] + fib[i - 1]
    fib.append(sum_of_numbers)
print(fib)
