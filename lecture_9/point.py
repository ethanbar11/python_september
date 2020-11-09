import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print('x: ', self.x, 'y: ', self.y)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((other_point.x - self.x) ** 2 +
                         (other_point.y - self.y) ** 2)

    def __add__(self, other_point):
        new_point = Point(self.x + other_point.x, self.y + other_point.y)
        return new_point


p1 = Point(1, 1)
p2 = Point(2, 3)
p1.show()
p2.show()
print(p2.dist(p1))
p3=p1+p2
p3.show()
