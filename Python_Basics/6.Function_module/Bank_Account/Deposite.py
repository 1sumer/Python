# deposit.py
from Account import BankAccount

def deposit(account, amount):
    """Deposits the given amount into the account."""
    if amount > 0:
        account.balance += amount
        print(f"{amount} deposited. New balance: {account.balance}")
    else:
        print("Deposit amount must be positive!")
