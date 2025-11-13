class Dog:
    """Model a simple dog"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name.title()} is now sitting. ")

    def shake(self):
        print(f'{self.name.title()} is shaking hands. ')


fido = Dog("fido", 3)
hudson = Dog("hudson", 10)
fido.sit()
hudson.sit()
hudson.shake()