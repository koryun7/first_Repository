# Define a class named BankAccount with an __init__ method that initializes two
# instance variables: account_holder and balance.
# The class has methods like deposit and withdraw, each of which takes an amount as
# an argument and updates the account balance accordingly. These methods also
# include checks for valid input and available funds.
# The get_balance method allows you to retrieve the account balance.
# We create an Object of the BankAccount class called account1 with an initial balance of $1000.
# We deposit $500 and withdraw $200 from the account and print the account information.
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Ավանդ, {amount}$ հաջողվեց։ Ընդհանուր գումար՛ {self.balance}$"
        else:
            return "Անվավաեր գումար։"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Կանխիկացում, {amount}$ հաջողվեց։ Ընդհանուր գումար՛ {self.balance}$"
        elif amount <= 0:
            return "Անվավաեր գումար։"
        else:
            return "Անբավարար միջոցներ։"

    def get_balance(self):
        return f"Ընթացիկ հաշվեկշիռ։ {self.balance}$"


account = BankAccount("Will Smith", 1000)


print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(1500))
print(account.deposit(-100))
print(account.get_balance())
