class Mammal:
    def __init__(self, mother_name):
        self.mother_name = mother_name

    def give_birth(self):
        print('Im giving birth! WOHO!')


class Dog(Mammal):
    def __init__(self, mother_name, dog_name):
        self.dog_name = dog_name
        super().__init__(mother_name)

    def bark(self):
        print('Im barking!')


dog = Dog('Hildy', 'Cooper')
dog.give_birth()
dog.bark()
