class Car:
    name = None
    make = None
    model = None

    def __init__(self, var_name, var_make, var_model):
        self.name = var_name
        self.make = var_make
        self.model = var_model

    def start_engine(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the model " + self.model)

lamborgini = Car("Lamborgini", "V2", "2024")
lamborgini.start_engine()

xuv = Car("XUV", "V6", "2023")
xuv.start_engine()