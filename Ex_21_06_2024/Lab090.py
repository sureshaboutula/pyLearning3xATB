# Decorators
# What is a decorator?
# A decorator is essentially a function that takes another function as argument and returns a new function by extending its behaviour


def my_decorator(func):
    def wrapper():
        print("Starting........")
        print("****************")
        func()
        print("****************")
        print("Ending........")

    return wrapper()

@my_decorator
def say_hello():
    print("Say Hello")