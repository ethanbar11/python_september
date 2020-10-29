def remove_dictionary_spaces(dict_with_spaces):
    dict_to_return = {}
    for key in dict_with_spaces.keys():
        new_key_name = key.replace(' ', '')
        dict_to_return[new_key_name] = dict_with_spaces[key]
    return dict_to_return


def remove_dictionary_spaces_same(dict_with_spaces):
    to_add = {}
    to_remove = []
    for key in dict_with_spaces.keys():
        new_key_name = key.replace(' ', '')
        if new_key_name != key:
            to_add[new_key_name] = dict_with_spaces[key]
            to_remove.append(key)
        else:
            pass
    dict_with_spaces.update(to_add)
    for key_to_delete in to_remove:
        del dict_with_spaces[key_to_delete]


first_dictionary = {'Hello !': 4, 'Bli Bla Blo': 10, 'Kika po': 'Hello'}
print(first_dictionary)
# second_dictionary = remove_dictionary_spaces(first_dictionary)
# print(second_dictionary)
remove_dictionary_spaces_same(first_dictionary)
print(first_dictionary)
