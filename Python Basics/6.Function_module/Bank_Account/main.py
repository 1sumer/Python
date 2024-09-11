# main.py
from Account import BankAccount
from Deposite import deposit
from Withdraw import withdraw
from Balance import display_balance

def main():
    # Create an account
    acc1 = BankAccount("John Doe", 500)

    # Perform deposit
    deposit(acc1, 300)

    # Perform withdrawal
    withdraw(acc1, 200)

    # Display balance
    display_balance(acc1)

if __name__ == "__main__":
    main()
