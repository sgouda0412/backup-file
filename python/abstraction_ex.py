from abc import ABC, abstractmethod


class Dog(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

    def display(self):
        print(f"Dog's name {self.name}")


class Labrador(Dog):
    def sound(self):
        print("Labrador wooof!!!")


class Beagle(Dog):
    def sound(self):
        print("Beagle Barks!!!")


dogs = [Labrador("Buddy"), Beagle("kuna")]
for dog in dogs:
    dog.display()
    dog.sound()


from abc import ABC, abstractmethod


# Define an abstract class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass  # This is an abstract method, no implementation here.


# Concrete subclass of Animal
class Dog(Animal):

    def sound(self):
        return "Bark"  # Providing the implementation of the abstract method


# Create an instance of Dog

dog = Dog()
print(dog.sound())  # Output: Bark
