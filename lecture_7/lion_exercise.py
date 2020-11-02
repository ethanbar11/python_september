import random


class Lion:
    def __init__(self, name):
        self.name = name

    def rawr(self):
        print('rawr ' + self.name)

    def sum(self, a, b):
        return a + b

    def __str__(self):
        return 'My name is ' + self.name

    def __repr__(self):
        return 'My name is ' + self.name


class Zoo:
    def __init__(self, ):
        self.lions = {}
        # self.lions = {}

    def add_lion(self, lion):
        # Lion is an object
        num = random.randint(1, len(lion.name))
        first_part = lion.name[:num]
        end_part = lion.name[num:]
        lion.name = first_part + '1' + end_part
        self.lions[lion.name] = lion

    def remove_lion(self, lion_name):
        if lion_name in self.lions:
            del self.lions[lion_name]

    def get_lion_amount(self):
        return len(self.lions)

    def get_longest_lion_name(self):
        longest_name = ''
        for name in self.lions.keys():
            if len(name) > len(longest_name):
                longest_name = name
        return longest_name


zoo = Zoo()
ethan = Lion('Ethan')
mor = Lion('Mor')
mor.rawr()
zoo.add_lion(ethan)
zoo.add_lion(mor)
print('Before', zoo.lions)
zoo.remove_lion(ethan.name)
print('After', zoo.lions)
print(ethan)
print(zoo.lions)
# print(mor.sum(1, 2))
