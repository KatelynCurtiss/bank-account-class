# Katelyn Curtiss
# April 6 2025
# Three Ways to Modify BankAccount Class Attributes

class BankAccount:
    def __init__(self, account_holder, balence):
        self.account_holder = account_holder
        self.balence = balence
        

    def BankAccount(self):
        return f"{self.account_holder}{self.balence}"
    
my_account = BankAccount('Account Holder: Katelyn Curtiss, ', 'Balence: $1500')
print(my_account.BankAccount())

my_account = BankAccount('After direct assignment:')
print(my_account.BankAccount())


   



