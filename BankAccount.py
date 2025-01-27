class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = balance
        
    #method to make deposits with error handling
    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.balance += amount
        except ValueError as e:
            print(f"Error: {e}")

    #method to make withdraws with error handling
    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > self.balance:
                raise ValueError("Insufficient funds.")
            self.balance -= amount
        except ValueError as e:
            print(f"Error: {e}")

    #prints balance
    def __str__(self):
        return f"Your account balance is ${self.balance:.2f}"


if __name__ == "__main__":
    account = BankAccount(100)
    print(account)

    account.deposit(50)
    print(account)

    account.withdraw(30)
    print(account)

    account.withdraw(150)  
    account.deposit(-10)
