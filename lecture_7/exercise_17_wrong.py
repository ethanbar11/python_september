def get_best_fruits():
    return 'pineapple', 'passion fruit',3


x,y=get_best_fruits()
x = get_best_fruits()
print(x)
print(type(x))
d = {'h': 5, 'gafa': True, 'Ffdaf': 'Woho'}

for tup in d.items():
    key, value = tup
    print(key, value)
    print(type(tup))

