# Encapsulation - bind the data variables with the methods

# Data Member - Class variables
# Methods - functions within the class
# Wrapping or binding the data variables with the methods is called Encapsulation
# OR
# Hide the data members(class variables/Instance variables) by using only methods.

class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when an Object is created")


xuv = Car()
xuv.password = "345" # We are able to change the class variable outside the class.
print(xuv.password)

# Apply encapsulation to above code
class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when an Object is created")

    def change_password(self):
        self.password = "345"

xuv = Car()
# xuv.password = "222" # Still able to access variable from outside of class. Data is not secure
print(xuv.password)
xuv.change_password()
print(xuv.password)


