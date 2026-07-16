from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, owner, balance=0.0):
        self._owner = owner
        self._balance = float(balance)

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        return self._balance

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def statement(self):
        pass

    def __str__(self):
        return self.statement()


class SavingsAccount(Account):
    def __init__(self, owner, balance=0.0, rate=0.05):
        super().__init__(owner, balance)
        self._rate = rate

    @property
    def rate(self):
        return self._rate

    def add_interest(self):
        interest = self._balance * self._rate
        self._balance += interest
        return interest

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds in SavingsAccount.")
        self._balance -= amount
        return self._balance

    def statement(self):
        return (
            f"SavingsAccount | Owner: {self._owner} | "
            f"Balance: {self._balance:.2f} | Rate: {self._rate:.2%}"
        )


class CurrentAccount(Account):
    def __init__(self, owner, balance=0.0, overdraft=0.0):
        super().__init__(owner, balance)
        self._overdraft = float(overdraft)

    @property
    def overdraft(self):
        return self._overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self._balance - amount < -self._overdraft:
            raise ValueError("Withdrawal exceeds overdraft limit.")
        self._balance -= amount
        return self._balance

    def statement(self):
        return (
            f"CurrentAccount | Owner: {self._owner} | "
            f"Balance: {self._balance:.2f} | Overdraft: {self._overdraft:.2f}"
        )


class BusinessAccount(Account):
    def __init__(self, owner, balance=0.0, credit_limit=0.0, monthly_fee=0.0):
        super().__init__(owner, balance)
        self._credit_limit = float(credit_limit)
        self._monthly_fee = float(monthly_fee)

    @property
    def credit_limit(self):
        return self._credit_limit

    @property
    def monthly_fee(self):
        return self._monthly_fee

    def apply_monthly_fee(self):
        self._balance -= self._monthly_fee
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self._balance - amount < -self._credit_limit:
            raise ValueError("Withdrawal exceeds business credit limit.")
        self._balance -= amount
        return self._balance

    def statement(self):
        return (
            f"BusinessAccount | Owner: {self._owner} | "
            f"Balance: {self._balance:.2f} | "
            f"Credit Limit: {self._credit_limit:.2f} | "
            f"Monthly Fee: {self._monthly_fee:.2f}"
        )


if __name__ == "__main__":
    accounts = [
        SavingsAccount("Estub", 1000, rate=0.08),
        CurrentAccount("Aman", 500, overdraft=300),
        BusinessAccount("Yango Corp", 5000, credit_limit=2000, monthly_fee=50),
    ]

    print("=== Initial Statements ===")
    for account in accounts:
        print(account)

    print("\n=== Transactions ===")
    try:
        accounts[0].deposit(200)
        accounts[0].withdraw(100)
        interest = accounts[0].add_interest()
        print(f"Savings interest added: {interest:.2f}")

        accounts[1].deposit(100)
        accounts[1].withdraw(700)

        accounts[2].withdraw(6000)
        accounts[2].apply_monthly_fee()

    except ValueError as e:
        print("Transaction error:", e)

    print("\n=== Final Statements ===")
    for account in accounts:
        print(account)

        a = SavingsAccount("Estub", 1000)
b = CurrentAccount("Aman", 500)
c = BusinessAccount("Yango corp", 5000)
a.deposit(100)
print(a.balance)  
print(b.balance)   
print(c.balance)   