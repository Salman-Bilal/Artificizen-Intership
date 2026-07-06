"""
Question: 2: Define a custom exception InsufficientBalanceError and raise it inside the BankAccount class from Day 4.

"""

class InsufficientBalanceError(Exception):
    def __init__(self, current_balance: float, requested_amount: float):
        self.current_balance = current_balance
        self.requested_amount = requested_amount
        self.shortfall = requested_amount - current_balance
        
        super().__init__(
            f"Transaction Declined! Attempted to withdraw ${requested_amount:,.2f}, "
            f"but current balance is ${current_balance:,.2f}. You are short by ${self.shortfall:,.2f}."
        )

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
            print(f"Current Balance is {self.Balance:,.2f}")   
        
    def withdrawal(self, amount):
        if amount <= 0:
            print("Please enter a valid amount")
            return False
        elif amount > self.Balance:
            raise InsufficientBalanceError(self.Balance, amount)
        else:
            self.Balance -= amount
            print(f"Remaining balance After Withdraw: {self.Balance:,.2f}")
            return True

my_account = BankAccount("Ahmad Afzal", 30000)

my_account.deposit(1000)
my_account.withdrawal(5000)      