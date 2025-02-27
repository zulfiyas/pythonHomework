import json
import random

class Account:
  def __init__(self, account_number, name, balance = 0.0):
    self.account_number = account_number
    self.name = name
    self.balance = balance
  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
    else:
      print("Invalid deposit amount. Amount must be greater than 0.")
  def withdraw(self, amount):
    if 0 < amount <= self.balance:
      self.balance -= amount
      print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
    else:
      print("Invalid withdrawal amount or insufficient funds.")
    
  def to_dict(self):
    return {
      "account_number": self.account_number,
      "name": self.name,
      "balance": self.balance
    }

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit=0.0):
        account_number = str(random.randint(10000, 99999)) 
        if account_number in self.accounts:
            return self.create_account(name, initial_deposit)  

        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"\nAccount Number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Balance: ${account.balance}\n")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            json.dump({acc: self.accounts[acc].to_dict() for acc in self.accounts}, file)

    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as file:
                data = json.load(file)
                self.accounts = {acc: Account(**data[acc]) for acc in data}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {} 

#checking time) 
def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Bank!")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            bank.create_account(name, initial_deposit)
        elif choice == "2":
            account_number = input("Enter account number: ")
            bank.view_account(account_number)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(account_number, amount)
        elif choice == "4":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(account_number, amount)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()