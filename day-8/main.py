from bank import *
from registry import AccountRegistry


registry = AccountRegistry()

sms = SMSAlert()
log = AuditLog()

a = AccountFactory.create("savings", "Selam ", 1001, 5000)
b = AccountFactory.create("current", "Eman", 1002, 1200)
c = AccountFactory.create("savings", "Sara", 1003, 9500)
d = AccountFactory.create("current", "John", 1004, 7000)

for account in [a, b, c, d]:
    account.subscribe(sms)
    account.subscribe(log)
    registry.add(account)

a.deposit(500)
a.withdraw(200)
a.deposit(1000)

print("========== Leaderboard ==========")

for account in registry.top_by_balance(3):
    print(account.owner, account.balance)

print()

print("========== Binary Search ==========")

found = registry.find_by_number(1003)

if found:
    found.show()

print()

print("========== Recursive Total ==========")

print(
    registry.total_transactions(a)
)