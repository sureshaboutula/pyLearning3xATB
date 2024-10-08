# Apply encapsulation/Access modifiers to functions

class Car:
    name = None

    def __init__(self):
        self.public_var = "public"
        self._protected_var = "protected123"
        self.__private_var = "private@123"

    def __private_method(self): # Private Method
        print("Protected!")
        print(self.public_var) # Able to access
        print(self._protected_var) # Able to access
        print(self.__private_var) # Able to access

    def printName(self):  #Public Method
        print("I am allowed")
        print(self.public_var) # Able to access
        print(self._protected_var) # Able to access
        print(self.__private_var) # Able to access
        self.__private_method() # Able to access the private method

alto = Car()
alto.public_var
alto._protected_var # Able to access but system wont suggest this variable
#alto.__private_var # # Not able to access private variable from outside of class
#alto.__private_method() # Not able to access private method from outside of class
alto.printName()
