# Without Encapsulation
class BankAccount:

    def __init__(self):
        self.balance = 0
        self.__private_var = 0

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print("Your balance is", self.balance)

icici = BankAccount()
print(icici.balance)
icici.deposit(101)
icici.show_balance()
icici.deposit(99)
icici.show_balance()
icici.withdraw(199)
icici.show_balance()
