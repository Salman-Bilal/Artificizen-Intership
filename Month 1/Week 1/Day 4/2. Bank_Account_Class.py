"""
Question: 2: Create a BankAccount class with deposit() and withdraw() methods; prevent withdrawals beyond the balance.

"""

class BankAccount:
    def __init__(self, AccountHolderName, Balance=0):
        self.AccountHolderName = AccountHolderName
        self.Balance = Balance


    def deposit(self, amount):
        if amount <= 0:
            print("Please enter a valid amount")
            return
        else:
            self.Balance += amount
            print(f"Current Balance is {self.Balance}")   
        
    def withdrawal(self, amount):
        if amount <= 0:
            print("Please enter a valid amount")
            return False
        elif amount > self.Balance:
            print("Insufficient Funds")
            return False
        else:
            self.Balance -= amount
            print(f"Remaining balance After Withdraw: {self.Balance}")
            return True

my_account = BankAccount("Ahmad Afzal", 30000)

my_account.deposit(1000)
my_account.withdrawal(5000)