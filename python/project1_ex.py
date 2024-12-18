# Base Class
class BankAccount:
    def __init__(self, account_holder: str, account_number: str, balance: float):
        self.__account_holder = account_holder  # Private attribute
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    # Getter for account holder
    def get_account_holder(self) -> str:
        return self.__account_holder

    # Getter for account number
    def get_account_number(self) -> str:
        return self.__account_number

    # Getter for balance
    def get_balance(self) -> float:
        return self.__balance

    # Deposit method (Encapsulation: manages balance securely)
    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive!")

    # Withdraw method (Encapsulation: prevents overdraft)
    def withdraw(self, amount: float) -> None:
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

# Derived Class 1: SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder: str, account_number: str, balance: float, interest_rate: float):
        super().__init__(account_holder, account_number, balance)
        self.__interest_rate = interest_rate  # Private attribute

    def add_interest(self) -> None:
        interest = self.get_balance() * self.__interest_rate / 100
        self.deposit(interest)
        print(f"Interest of {interest} added at rate {self.__interest_rate}%.")

# Derived Class 2: CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_holder: str, account_number: str, balance: float, overdraft_limit: float):
        super().__init__(account_holder, account_number, balance)
        self.__overdraft_limit = overdraft_limit  # Private attribute

    # Overriding withdraw method to allow overdraft
    def withdraw(self, amount: float) -> None:
        if amount > 0 and amount <= self.get_balance() + self.__overdraft_limit:
            new_balance = self.get_balance() - amount
            if new_balance < 0:
                print(f"Overdraft used. Overdraft limit remaining: {self.__overdraft_limit + new_balance}")
            super().withdraw(amount)
        else:
            print("Invalid withdrawal amount or overdraft limit exceeded.")

# Example Usage
def main():
    # Creating a savings account
    savings = SavingsAccount("Alice", "SA123", 1000.0, 5.0)
    print(f"Savings Account Holder: {savings.get_account_holder()}")
    savings.deposit(500)
    savings.add_interest()
    savings.withdraw(300)

    print("\n")

    # Creating a checking account
    checking = CheckingAccount("Bob", "CA456", 500.0, 200.0)
    print(f"Checking Account Holder: {checking.get_account_holder()}")
    checking.withdraw(600)  # Overdraft
    checking.withdraw(200)  # Exceeds overdraft limit
    checking.deposit(300)

if __name__ == "__main__":
    main()
