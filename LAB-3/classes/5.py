class BankAccount:
    def  __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} deposited to the account of {self.owner}. New balance: {self.balance}')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'{amount} withdrawn from the account of {self.owner}. New balance: {self.balance}')
        else:
            print(f'Insufficient balance. Withdrawal not possible.')

account = BankAccount("John", 1000)

account.deposit(500)
account.deposit(300)

account.withdraw(600)
account.withdraw(700)
