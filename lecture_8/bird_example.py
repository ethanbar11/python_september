class Bird:
    def __init__(self):
        self.wing_color = 'Blue'

    def __str__(self):
        return "Im awesome"


bird1 = Bird()
print('Bird 1 :', bird1)
lst = [1, 2, 3]
print(lst)
print(type(bird1))
print(type(lst))
# bird1.wing_size = 50
# print(bird1.wing_size)
# bird2=Bird()
# print(bird2.wing_size)
