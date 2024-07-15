# small_town_teller
# Author: [Peter Van Beever]
# Version: 1.0.0
# Description: 

class Person:
    def __init__(self, id: int, first_name: str, last_name: str):
        # variables
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

class Account:
    def __init__(self, number: int, type: str, owner: Person, balance: float = 0.0):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance

class Bank:
    # create dictionaries to store data
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    # add customer, customer id  unique
    def add_customer(self, person):
        if person.id in self.customers:
            raise ValueError("Customer ID must be unique.")
        self.customers[person.id] = person
    
    # add account, account number unique, owner  registered
    def add_account(self, account):
        if account.owner.id not in self.customers:
            raise ValueError("Owner must be customer already.")
        if account.number in self.accounts:
            raise ValueError("Account number must be unique.")
        self.accounts[account.number] = account

    # remove account, account must exist
    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
        else:
            raise ValueError("Account not found")

    # locate account number, update balance
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].balance += amount
        else:
            raise ValueError("Account not found")
    
    # locate account number, check funds, update balance
    def withdrawal(self, account_number, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if account.balance >= amount:
                account.balance -= amount
            else:
                raise ValueError("Insufficient funds in your account")
        else:
            raise ValueError("Account not found")

    # check account number, return balance
    def balance_inquiry(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].balance
        else:
            raise ValueError("Account not found")