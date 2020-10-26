x = {'Mor': 100, 'Omer': 47, 'Ori': 350, 'Yael': 700}
x['Ethan'] = 10
del x['Ethan']
for i in x.keys():
    print(i,x[i])
print(x.keys())
x[5]='Hello'
print(x)