class MyClass:

    def __init__(self):
        self.name = "Amit" # Public variable
        self.__email = "amit@gmail.com"

    def public_func(self):
        print("Public Func()")

    def __private_func(self):
        print("This is private function. You can only access me via another public method")

    def public_fn_private(self):
        self.__private_func()

# Security - Not everyone can access your variables/methods

a = MyClass()
a.name
#a.__email # AttributeError: 'MyClass' object has no attribute '__email'
a.public_func()
a.public_fn_private()
#a.__private_func() # AttributeError: 'MyClass' object has no attribute '__private_func'