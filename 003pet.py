# object orientated programming in Python

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("What am I?")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and {self.color}.")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.show()
p.speak()
c = Cat("Bill", 12, "Yellow")
c.show()
c.speak()
d = Dog("Jill", 23)
d.show()
d.speak()
f = Fish("Bubbles", 10)
f.show()
f.speak()