import random

correct_number = random.randint(1, 9)
counter = 0
guessed_number = ''
while guessed_number != correct_number:
    guessed_number = input('Enter number: ')
    if guessed_number == 'exit':
        break
    elif int(guessed_number) >correct_number:
        print('Too high')
    elif int(guessed_number) < correct_number:
        print('Too low')
    else:
        print('Exactly RIGHT! YES!')
    counter += 1
print(counter)