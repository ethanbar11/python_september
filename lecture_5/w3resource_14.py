letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

letters_counter = 0
numbers_counter = 0
message = input('Insert string: ')
for letter in message:
    if letter in letters:
        letters_counter += 1
    elif letter in numbers:
        numbers_counter += 1

print('Letters amount :', letters_counter, ' Numbers amount :', numbers_counter)
