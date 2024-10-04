# class Dog:
#     name = None
#     id = None
#     def sleep(self):
#         print("sleeping")
#
# dog1 = Dog()
# print(dog1.name)
# dog1.name = "Chow"
# print(dog1.name)
# dog1.sleep()
#
# dog2 = Dog()
# print(dog2.name)
# dog2.name = "Mow"
# print(dog2.name)

# Constructor - will be used to initialize the values of the instance variables/ttributes
# Rewrite above code with constructor

class Dog:
    name = None
    id = None

    #Constructor Function
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def sleep(self):
        print("Who is sleeping?", self.name)

dog1 = Dog("Chow", "1")
print(f"{dog1.name} has ID {dog1.id}")
dog1.sleep()

dog2 = Dog("Mow", "2")
print(f"{dog2.name} has ID {dog2.id}")
dog2.sleep()