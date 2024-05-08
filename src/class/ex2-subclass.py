class Animal:
    def __init__(self, name, age, animal_type):
        self.name = name
        self.age = age
        self.animal_type = animal_type

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Type: {self.animal_type}")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Mammal")

    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Mammal")

    def make_sound(self):
        return "Meow!"


class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Bird")

    def make_sound(self):
        return "Chirp!"

if __name__ == "__main__":
    # Create a Dog object
    my_dog = Dog("Buddy", 5)
    my_dog.display_info()       # Name: Buddy, Age: 5, Type: Mammal
    print(my_dog.make_sound())  # Woof!

    # Create a Cat object
    my_cat = Cat("Whiskers", 3)
    my_cat.display_info()       # Name: Whiskers, Age: 3, Type: Mammal
    print(my_cat.make_sound())  # Meow!

    # Create a Bird object
    my_bird = Bird("Pepper", 1)
    my_bird.display_info()      # Name: Pepper, Age: 1, Type: Bird
    print(my_bird.make_sound()) # Chirp!

