import pickle

class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

class Account:
    def __init__(self, number, account_type, owner, balance):
        self.number = number
        self.type = account_type
        self.owner = owner
        self.balance = balance

class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self, person):
        if person.id in self.customers:
            raise ValueError("Customer ID must be unique.")
        self.customers[person.id] = person
    
    def add_account(self, account):
        if account.owner not in self.customers:
            raise ValueError("Owner must be customer already.")
        if account.number in self.accounts:
            raise ValueError("Account number must be unique.")
        self.accounts[account.number] = account

    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
        else:
            raise ValueError("Account not found")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].balance += amount
        else:
            raise ValueError("Account not found")
    
    def withdrawal(self, account_number, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if account.balance >= amount:
                account.balance -= amount
            else:
                raise ValueError("Insufficient funds in your account")
        else:
            raise ValueError("Account not found")

    def balance_inquiry(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].balance
        else:
            raise ValueError("Account not found")
        
    def save_data(self, file_path = 'bank_data.pickle'):
        data = {
            'customers': self.customers,
            'accounts': self.accounts
        }
        print(f"Saving data to {file_path}") 
        try:
            PersistenceUtils.write_pickle(file_path, data)
        except Exception as e:
            print(f"Error saving data: {e}") 

    def load_data(self, file_path = 'bank_data.pickle'):
        try:
            data = PersistenceUtils.load_pickle(file_path)
            self.customers = data['customers']
            self.accounts = data['accounts']
    
        except Exception as e:
            print(f"Error loading data: {e}") 

class PersistenceUtils:
    @staticmethod
    def write_pickle(file_path, data):
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)

    @staticmethod
    def load_pickle(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)
        
