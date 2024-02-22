class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance

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
            self.balance += self.balance * self.int_rate
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}  # Dictionary to hold multiple accounts

    def create_account(self, account_name, int_rate=0.02, balance=0):
        self.accounts[account_name] = BankAccount(int_rate, balance)

    def make_deposit(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
            print(f"Deposited ${amount} into {account_name}")
        else:
            print(f"Account '{account_name}' not found.")

    def make_withdrawal(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
            print(f"Withdrew ${amount} from {account_name}")
        else:
            print(f"Account '{account_name}' not found.")

    def display_user_balance(self, account_name):
        if account_name in self.accounts:
            print(f"User: {self.name}, Account: {account_name}")
            self.accounts[account_name].display_account_info()
        else:
            print(f"Account '{account_name}' not found.")

    def transfer_money(self, amount, other_user, from_account, to_account):
        if from_account in self.accounts and to_account in other_user.accounts:
            if self.accounts[from_account].balance >= amount:
                self.accounts[from_account].withdraw(amount)
                other_user.accounts[to_account].deposit(amount)
                print(f"Transferred ${amount} from {from_account} to {to_account}")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Account not found for transfer.")

# Example Usage
user1 = User("Alice", "alice@example.com")
user1.create_account("Savings", balance=500)
user1.create_account("Checking", balance=1000)

user2 = User("Bob", "bob@example.com")
user2.create_account("Savings", balance=300)
user2.create_account("Investment", balance=2000)

user1.make_deposit("Savings", 200)
user1.make_withdrawal("Checking", 100)
user1.display_user_balance("Savings")
user1.display_user_balance("Checking")

user1.transfer_money(150, user2, "Savings", "Savings")
user1.display_user_balance("Savings")
user2.display_user_balance("Savings")
