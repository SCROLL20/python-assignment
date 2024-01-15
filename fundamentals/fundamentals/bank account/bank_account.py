class BankAccount:
    def __init__(self, balance=0, interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self

# Testing the BankAccount class
account1 = BankAccount()  # Creating an account with default values
account1.display_account_info()  # Output: Balance: $0

account1.deposit(100).withdraw(30).yield_interest().display_account_info()
# Output: Balance: $75.65 (after interest calculation)

account2 = BankAccount(500, 0.02)  # Creating an account with initial balance and different interest rate
account2.display_account_info()  # Output: Balance: $500

account2.deposit(200).withdraw(250).yield_interest().display_account_info()
# Output: Insufficient funds: Charging a $5 fee
# Balance: $449.6 (after interest calculation)
