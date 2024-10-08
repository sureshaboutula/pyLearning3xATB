class Car:
    name = None

    def __init__(self):
        self.public_var = "public"
        self._protected_var = "protected123"
        self.__private_var = "private@123"


alto = Car()
alto_pub = alto.public_var = "updated_public" # Able to access the data from outside
print(alto_pub)
alto_pro = alto._protected_var = "updated_protected"
print(alto_pro)
alto_pri = alto.__private_var = "updated_private"
print(alto_pri)

# 3 types of access modifiers
# 1. Public
# 2. Protected - _
# 3. Private - __