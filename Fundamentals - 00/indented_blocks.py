def withdraw(amount):
    balance = 1000

    if balance >= amount:
        print("Withdraw successful")
    else:
        print("Insufficient funds")
    
    print("Thanks for using our service")

def deposit(amount):
        balance = 1000
        balance += amount
        print("Deposit successful")
    
withdraw(100)