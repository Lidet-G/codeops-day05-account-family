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

    
    # Find Account (Dictionary Lookup)
    # O(1)
   

    def find(self, number):

        return self.by_number.get(number)

    
    # List All Accounts
   

    def list_all(self):

        accounts = []

        for number in self.order:
            accounts.append(self.by_number[number])

        return accounts

    
    # Remove Account
  

    def remove(self, number):

        if number not in self.by_number:
            print("Account not found.")
            return

        del self.by_number[number]
        self.order.remove(number)

        print("Account removed.")

   
    # Total Accounts
    

    def total_accounts(self):

        return len(self.by_number)

   
    # Top N Accounts by Balance
    # O(n log n)


    def top_by_balance(self, n=5):

        return sorted(
            self.by_number.values(),
            key=lambda account: account.balance,
            reverse=True
        )[:n]

   
    # Binary Search
    # O(log n)
 

    def binary_search(self, numbers, target):

        low = 0
        high = len(numbers) - 1

        while low <= high:

            mid = (low + high) // 2

            if numbers[mid] == target:
                return mid

            elif numbers[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return -1

    # Find Account using Binary Search
    # O(log n)


    def find_by_number(self, number):

        sorted_numbers = sorted(self.by_number.keys())

        index = self.binary_search(
            sorted_numbers,
            number
        )

        if index == -1:
            return None

        return self.by_number[
            sorted_numbers[index]
        ]

    # Recursive Total Transactions


    def total_transactions(self, account):

        amounts = []

        for transaction_type, amount in account.history:
            amounts.append(amount)

        return self._recursive_sum(amounts)


    # Recursive Helper

    def _recursive_sum(self, amounts):

        # Base Case
        if not amounts:
            return 0

        # Recursive Case
        return amounts[0] + self._recursive_sum(amounts[1:])