def remove_duplicate_values_from_dict(dup_dict):
    duplicated_keys_to_delete = []
    for key in dup_dict.keys():
        if key not in duplicated_keys_to_delete:
            for inner_key in dup_dict.keys():
                if dup_dict[inner_key] == dup_dict[key] and inner_key != key:
                    duplicated_keys_to_delete.append(inner_key)

    for key_to_delete in duplicated_keys_to_delete:
        del dup_dict[key_to_delete]


d = {'a': 5, 'b': 10, 'c': 5, 'd': 12, 'e': 10}
print(d)
remove_duplicate_values_from_dict(d)
print(d)
