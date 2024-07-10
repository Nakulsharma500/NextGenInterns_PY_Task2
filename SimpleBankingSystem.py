class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance=0):
        if account_number in self.accounts:
            print("Account number already exists. Please use a different account number.")
        else:
            new_account = Account(account_number, account_holder, initial_balance)
            self.accounts[account_number] = new_account
            print(f"Account created successfully for {account_holder} with account number {account_number}")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account does not exist.")

    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)

    def withdraw(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.withdraw(amount)

    def check_balance(self, account_number):
        account = self.get_account(account_number)
        if account:
            account.check_balance()

    def display_accounts(self):
        print(f"Accounts in {self.bank_name}:")
        for account_number, account in self.accounts.items():
            print(f"Account Number: {account_number}, Account Holder: {account.account_holder}")


# Example usage:
def main():
    bank = Bank("State Bank of India")

    # Creating accounts
    bank.create_account("001", "Nakul Sharma", 1000)
    bank.create_account("002", "Ram sharma")

    # Depositing and withdrawing
    bank.deposit("001", 500)
    bank.withdraw("001", 200)

    bank.deposit("002", 1500)
    bank.withdraw("002", 300)

    # Checking balances
    bank.check_balance("001")
    bank.check_balance("002")

    # Displaying all accounts in the bank
    bank.display_accounts()


if __name__ == "__main__":
    main()
