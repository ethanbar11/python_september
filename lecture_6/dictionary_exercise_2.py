dict1 = {'A': 1, 'B': 2}
dict2 = {'C': 3, 'D': 4}
dict3 = {'E': 5, 'F': 6}

# Option 1
dict3.update(dict2)
dict3.update(dict1)
print(dict3)

# Option 2
for key in dict1.keys():
    dict3[key] = dict1[key]

for key in dict2.keys():
    dict3[key] = dict2[key]
