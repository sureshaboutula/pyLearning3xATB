# With Encapsulation
class BankAccount:

    def __init__(self):
        self.__balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.__balance += amount

    def __withdraw(self, amount):
        self.__balance -= amount

    def __show_balance(self):
        print("Your balance is", self.__balance)

    def if_you_are_authenticated(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("Not Allowed")

    def if_you_are_authenicated_user(self, auth, amount):
        if auth:
            self.__withdraw(amount=amount)
        else:
            print("Not Allowed")

icici = BankAccount()
icici.deposit(100)

secret_pin = input("Enter your pin : ")
if secret_pin == "3390":
    icici.if_you_are_authenticated(True)
else:
    icici.if_you_are_authenticated(False)

secret_pass = input("Enter your to withdraw : ")
amount_to_withdraw = int(input("Enter the withdraw amount : "))

if secret_pin == "3390":
    icici.if_you_are_authenicated_user(True, amount_to_withdraw)
    icici.if_you_are_authenticated(True)
else:
    icici.if_you_are_authenicated_user(False)
