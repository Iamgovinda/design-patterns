from abc import ABC, abstractmethod


# Abstract product
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# Concrete products
class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Factory class
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")


# Client code
animal = AnimalFactory.create_animal("cat")
print(animal.speak())  # Output: Woof!
