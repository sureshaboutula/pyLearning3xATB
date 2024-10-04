# Constructor with default attribute values
# Default - None
# class Dog:
#     name = None
#     id = None
#
#     #Constructor Function
#     def __init__(self, name=None, id=None):
#         self.name = name
#         self.id = id
#     def sleep(self):
#         print("Who is sleeping?", self.name)
#
# dog1 = Dog("Chow", "1")
# print(f"{dog1.name} has ID {dog1.id}")
# dog1.sleep()
#
# dog2 = Dog()
# print(f"{dog2.name} has ID {dog2.id}")
# dog2.sleep()

# Default Values

class Dog:
    name = None
    id = None

    #Constructor Function
    def __init__(self, name="Puppy", id="100"):
        self.name = name
        self.id = id
    def sleep(self):
        print("Who is sleeping?", self.name)

dog1 = Dog("Chow", "1")
print(f"{dog1.name} has ID {dog1.id}")
dog1.sleep()

dog2 = Dog()
print(f"{dog2.name} has ID {dog2.id}")
dog2.sleep()
