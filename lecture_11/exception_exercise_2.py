def get_char_type(c):
    ascii_value = ord(c)
    if 97 <= ascii_value <= 122:  # small characters
        return 0
    elif 64 <= ascii_value <= 90:  # big characters
        return 1
    elif 48 <= ascii_value <= 57:  # digits
        return 2
    elif 33 <= ascii_value <= 47 or 58 <= ascii_value <= 64:  # special
        return 3
    else:  # Other, for example space
        return 4


def print_string_types(s):
    type_amounts = [0, 0, 0, 0]
    for c in s:
        index_in_type_amounts = get_char_type(c)
        if index_in_type_amounts != 4:
            type_amounts[index_in_type_amounts] += 1
    print('Small characters:', type_amounts[0])
    print('Big characters:', type_amounts[1])
    print('Digits :', type_amounts[2])
    print('Other :', type_amounts[3])


def change_letters_size(s, to_lower_number):
    if type(s) != str:
        raise TypeError("S should be a string!")
    if type(to_lower_number) != int:
        raise TypeError("to_lower_number should be int!")
    if to_lower_number < 1 or to_lower_number > 2:
        raise ValueError("to_lower_number is not the right range! should be 1,2")
    print_string_types(s)
    if to_lower_number == 1:
        return s.lower()
    else:
        return s.upper()


try:
    print(change_letters_size('Hello! 1234, mmm nice to be here', 5))
except TypeError as e:
    print('Writing to file' + str(e))

except ValueError as e:
    f = 213124 + 1324512345 * 3
    print(f)
    print(e)
# try:
#     print('woho')
#     raise IndexError("I wohoed too much!")
#     print('Wohoing some more')
# except IndexError as e:
#     print('woho')
# exc
# except Exception as e:
#     print(e)
#     print('not wohing so much')
