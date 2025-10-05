class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.initial_balance = 0 # default attribute value

    def deposit(self, amount):
        account_bal = self.account_balance + amount
        self.initial_balance += account_bal
        return self.initial_balance
    
    def withdraw(self, amount):
        account_bal = self.account_balance - amount
        self.initial_balance -= account_bal
        return self.initial_balance
    
    def display_balance(self):
        print(f"The current balance is {self.initial_balance}")


    