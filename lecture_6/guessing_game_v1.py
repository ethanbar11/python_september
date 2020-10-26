print('Please choose number')
counter = 0
for i in range(101):
    print('Your number is', i)
    answer = input('Is it? : ')
    if answer == 'yes':
        print('I found the number! Its', i)
        counter = i + 1
        break
print('The amount of the numbers i tried is:', counter)
