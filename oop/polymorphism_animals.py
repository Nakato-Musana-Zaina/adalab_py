class Animal:
    def move(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def move(self):
        print("Flying")

    def make_sound(self):
        print("chirp")

class Cat(Animal):
    def move(self):
        print("walks")

    def make_sound(self):
        print("mew")

class Fish(Animal):
    def move(self):
        print("swimming")

    def make_sound(self):
        print("bop")

