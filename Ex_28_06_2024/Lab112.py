class Person:
    # Class variables/Instance variables
    name = "Amit"
    age = None

    def walk(self):
        a = 10 # Local variable
        print("I am a method")
        print("Hi", self.age)

amit = Person()
amit.walk()