class Person:
    # Attributes
    name = None
    id = None
    age = None
    phone_number = None

    # Behaviour
    # ObjectRef = Object -> ClassName()
    def talk(self): # No Arg, No return
        print("I can talk....")
    def sleep(self, name): # 1 Arg, No return
        print("I am a method!!")
        print("Sleep", name)

    def sleep2(self, name): # 1 Arg, return
        print("I am a method!!")
        return None
    def walk(self): # No Arg, No Return
        print("I am walking")

    def walk_return(self): # No Arg, Return
        return "I am walking"

# Create Object of the person

suresh = Person()
suresh.name = "Suresh Ab"
suresh.talk()

ritika = Person()
ritika.name = "Ritika Gupta"
ritika.walk()