class Lion:
    def __init__(self, name):
        self.name = name

    def rawr(self):
        print('rawr ' + self.name)

    def sum(self, a, b):
        return a + b


class Zoo:
    def __init__(self):
        self.lions = {}

    def add_lion(self, lion):
        # Lion is an object
        self.lions[lion.name] = lion

    def remove_lion(self, lion_name):
        if lion_name in self.lions:
            del self.lions[lion_name]

    def get_lion_amount(self):
        return len(self.lions)


zoo = Zoo()
ethan_lion = Lion('Ethan')
zoo.add_lion(ethan_lion)
ethan = Lion('Ethan')
mor = Lion('Mor')
ethan.rawr()
print(mor.sum(1, 2))
