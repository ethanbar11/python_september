import json


# Exercise 2

class Dog:
    def __init__(self, name, age, dog_type, is_loving_cats):
        self.name = name
        self.age = age
        self.dog_type = dog_type
        self.is_loving_cats = is_loving_cats


def convert_dog_to_dictionary(obj):
    if isinstance(obj, Dog):
        # Option A
        return obj.__dict__

        # Option B
        return {'name': obj.name, 'age': obj.age}  # ...}


dog = Dog('Ethan', 25, 'Sibiriean Haski', True)
with open('dog_json.json', 'w') as f:
    dog_str = json.dumps(dog, default=convert_dog_to_dictionary)
    f.write(dog_str)
