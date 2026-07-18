from bank import Account

class AccountRegistry:

    def __init__(self):

       
        self.by_number = {}

        self.order = []

    # Add Account
    # O(1)
    
    def add(self, account):

        if account.number in self.by_number:
            print("Account already exists.")
            return

        self.by_number[account.number] = account
        self.order.append(account.number)

    # Find Account
    # O(1)
  

    def find(self, number):

        return self.by_number.get(number)

    # List All Accounts
    

    def list_all(self):

        accounts = []

        for number in self.order:
            accounts.append(self.by_number[number])

        return accounts

    def remove(self, number):

        if number not in self.by_number:
            print("Account not found.")
            return

        del self.by_number[number]
        self.order.remove(number)

        print("Account removed.")

    def total_accounts(self):

        return len(self.by_number)