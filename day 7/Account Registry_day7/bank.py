from abc import ABC


class BankConfig:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000

        return cls._instance


class SMSAlert:

    def update(self, message):
        print("[SMS]", message)


class AuditLog:

    def update(self, message):
        print("[LOG]", message)


class Account(ABC):

    def __init__(self, owner, number, balance):

        self.owner = owner
        self.number = number
        self.balance = balance

        self.observers = []

        self.history = []

   

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):

        for observer in self.observers:
            observer.update(message)

   

    def deposit(self, amount):

        self.balance += amount

        self.history.append(("deposit", amount))

        self.notify(f"{self.owner} deposited {amount} ETB")


    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance -= amount

            self.history.append(("withdraw", amount))

            self.notify(f"{self.owner} withdrew {amount} ETB")

        else:

            print("Insufficient Balance")


    def undo_last(self):

        if not self.history:
            print("No transaction to undo.")
            return

        transaction, amount = self.history.pop()

        if transaction == "deposit":

            self.balance -= amount

            self.notify(
                f"Undo Deposit: {amount} ETB removed"
            )

        elif transaction == "withdraw":

            self.balance += amount

            self.notify(
                f"Undo Withdrawal: {amount} ETB restored"
            )


    def show(self):

        print("---------------------------")
        print("Owner   :", self.owner)
        print("Number  :", self.number)
        print("Balance :", self.balance)


class SavingsAccount(Account):

    def add_interest(self):

        config = BankConfig()

        interest = self.balance * config.interest_rate

        self.balance += interest

        self.notify("Interest Added")


class CurrentAccount(Account):

    def withdraw(self, amount):

        config = BankConfig()

        if self.balance + config.overdraft_limit >= amount:

            self.balance -= amount

            self.history.append(("withdraw", amount))

            self.notify(f"{self.owner} withdrew {amount} ETB")

        else:

            print("Overdraft Limit Exceeded")


class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance=0):

        if kind == "savings":

            return SavingsAccount(
                owner,
                number,
                balance
            )

        elif kind == "current":

            return CurrentAccount(
                owner,
                number,
                balance
            )

        else:

            raise ValueError(
                "Invalid Account Type"
            )