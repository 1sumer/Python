# balance.py
from Account import BankAccount

def display_balance(account):
    """Displays the current account balance."""
    print(f"{account.owner}'s account balance: {account.balance}")
