def check_if_string_containg_character_of_other_string(str1, str2):
    for c in str1:
        if c in str2:
            return True
    return False


# print(check_if_string_containg_character_of_other_string('boha', 'bkkk'))


def is_password_valid(password):
    small_letters = 'abcdefghijklmnopqrstuvwxyz'
    big_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(password) < 6:
        return False
    if len(password) > 16:
        return False
    is_containing_small_letter = \
        check_if_string_containg_character_of_other_string \
            (password, small_letters)
    if not is_containing_small_letter:
        return False
    is_containing_big_letter = \
        check_if_string_containg_character_of_other_string \
            (password, big_letters)
    if not is_containing_small_letter:
        return False
    return True


'Woho'
a = 5
lst = [1, 2, 3, 4]
if a in lst:
    print('1 is in lst!')
else:
    print('a is not in lst!')

x = True
y = 5
password = input('Please enter a password')
