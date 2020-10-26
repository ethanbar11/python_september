import math

def a():
    print('Woho')
    x=5+3

print('Please choose number')
counter = 0
should_i_run = True
a()
left = 0
right = 100
guess = (right + left) / 2

while should_i_run:
    counter += 1
    answer = input('Is your number ' + str(guess)+ ' ')
    if answer == 'yes':
        should_i_run = False
    elif answer == 'Too low':
        left = guess + 1
    elif answer == 'Too high':
        right = guess - 1
    guess = (right + left) // 2
print('The amount of the numbers i tried is:', counter)
