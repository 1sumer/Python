# withdraw.py
from Account import BankAccount

def withdraw(account, amount):
    """Withdraws the given amount from the account."""
    if 0 < amount <= account.balance:
        account.balance -= amount
        print(f"{amount} withdrawn. New balance: {account.balance}")
    else:
        print("Invalid withdraw amount!")
