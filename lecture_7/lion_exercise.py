class Lion:
    def __init__(self, name):
        self.name = name

    def rawr(self):
        print('rawr ' + self.name)

    def sum(self, a, b):
        return a + b


class Zoo:
    def __init__(self):
        self.lions = []

    def add_lion(self, lion_name):
        lion = Lion(lion_name)
        self.lions.append(lion)


ethan = Lion('Ethan')
mor = Lion('Mor')
ethan.rawr()
print(mor.sum(1, 2))
