# object orientated programming in Python

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

dogs_name = ["Tim", "Bill"]
dogs_age = [3, 2]

d = Dog(dogs_name[0], dogs_age[0])

print(f'{d.get_name()}: {d.get_age()} years old.')