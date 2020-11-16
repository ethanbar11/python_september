import pickle

# lst = [1, True, 'Hello', 'Shalom', 25, []]
path = 'binary_file.bin'
# with open(path, 'wb') as file_obj:
#     pickle.dump(lst, file_obj)
with open(path, 'rb') as f:
    lst = pickle.load(f)
    print(lst)
