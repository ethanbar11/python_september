class Vegito:
    def __init__(self, height):
        self.height = height

    def __str__(self):
        return 'Vegito height is :' + str(self.height)

    def __add__(self, other):
        combined_height = self.height + other.height
        vegito_to_return = Vegito(combined_height)
        return vegito_to_return


class Songuko:
    def __init__(self, power):
        self.power = power


v1 = Vegito(50)
v2 = Vegito(100)
songuko = Songuko(50)

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = lst1 + lst2
print(lst3)
# SAME!
# v3 = v1.__add__(v2)
v3 = v1 + v2
v4 = v1.__add__(v2).__add__(v3)
v4 = v1 + v2 + v3
print(v3)
