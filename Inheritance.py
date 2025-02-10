#Parent/Super class

class animal:
    def speak(self):
        print('Animal is speaking')

#Child class/Sub class/Derived class
class Dog(animal):
    def bark(self):
        print('dog is barking')

class Cat(Dog):
    def meow(self):
        print('Cat is meowing')

a = animal()

d = Dog()

c = Cat()

