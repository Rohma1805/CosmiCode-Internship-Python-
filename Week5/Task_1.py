#Task_1:
#Step 1:Define the BankAccount class (blueprint)
class BankAccount: 
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name 
        self.balance = balance
    #Method 1:Deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")
    #Method 2:Withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
    #Method 3:Transfer money to another account
    def transfer(self, other_account, amount):
        if amount > self.balance:
            print("Transfer failed! Insufficient balance.")
        else:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transferred {amount} to {other_account.owner_name}. Your new balance: {self.balance}")
#Step 2:Create objects (actual bank accounts)
account1 = BankAccount("001", "Rohma", 5000)
account2 = BankAccount("002", "Usman", 3000)
#Step 3:Use the methods
account1.deposit(2000)
account1.withdraw(1000)
account1.transfer(account2, 1500)
#Step 4:Check final balances
print(f"Final Balance of {account1.owner_name}: {account1.balance}")
print(f"Final Balance of {account2.owner_name}: {account2.balance}")