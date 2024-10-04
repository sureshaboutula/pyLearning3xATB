# Default constructor

class Dog:
    name = None
    id = None

    def __int__(self): # This is default constructor
        print("Default No Argument")
    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id
    def sleep(self):
        print("Sleepig")

dog1 = Dog("Chow", "1")
dog2 = Dog()
print(dog1.name)
print(dog1.id)
print(dog2.name)
print(dog2.id)