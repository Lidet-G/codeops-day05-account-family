from bank import AccountFactory, SMSAlert, AuditLog
from registry import AccountRegistry


def main():

    registry = AccountRegistry()

    sms = SMSAlert()
    log = AuditLog()

    # Create Accounts
    
    accounts = [

        AccountFactory.create(
            "savings",
            "Selam",
            1001,
            5000
        ),

        AccountFactory.create(
            "current",
            "Eman",
            1002,
            1200
        ),

        AccountFactory.create(
            "savings",
            "Sara",
            1003,
            9500
        ),

        AccountFactory.create(
            "current",
            "John",
            1004,
            7000
        ),

        AccountFactory.create(
            "savings",
            "Mahi",
            1005,
            4300
        )
    ]

   
    # Register Accounts
   

    for account in accounts:

        account.subscribe(sms)
        account.subscribe(log)

        registry.add(account)


    # Transactions
    

    accounts[0].deposit(1000)
    accounts[0].withdraw(500)
    accounts[0].deposit(300)

    accounts[1].deposit(700)

    accounts[2].withdraw(1000)


    # TEST 1
   
    print("\n===== TEST 1 =====")
    print("Total Accounts")

    print(registry.total_accounts())

    # TEST 2
  
    print("\n===== TEST 2 =====")
    print("Dictionary Lookup")

    account = registry.find(1004)

    if account:
        account.show()

    # TEST 3
 
    print("\n===== TEST 3 =====")
    print("Binary Search")

    account = registry.find_by_number(1003)

    if account:
        account.show()


    # TEST 4


    print("\n===== TEST 4 =====")
    print("Top 3 Balances")

    leaderboard = registry.top_by_balance(3)

    for account in leaderboard:

        print(
            account.owner,
            account.balance
        )

    # TEST 5

    print("\n===== TEST 5 =====")
    print("Recursive Transaction Total")

    print(
        registry.total_transactions(
            accounts[0]
        )
    )

    # TEST 6
   
    print("\n===== TEST 6 =====")
    print("Undo Last Transaction")

    accounts[0].undo_last()

    accounts[0].show()

    # TEST 7
   
    print("\n===== TEST 7 =====")
    print("Remove Account")

    registry.remove(1002)

    print(registry.total_accounts())

    # TEST 8
  
    print("\n===== TEST 8 =====")
    print("All Accounts")

    for account in registry.list_all():

        account.show()


if __name__ == "__main__":
    main()