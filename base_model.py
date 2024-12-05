class BankAccount:
    MAXIMAL_WITHDRAW = 1000.0

    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.MAXIMAL_WITHDRAW:
            raise MaximalWithdrawException(amount)

        if amount > self.balance:
            raise OverdraftMaxException(amount)

        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeDepositException(amount)

        self.balance += amount
        return self.balance

class MaximalWithdrawException(Exception):
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"The amount of money you want to withdraw is {self.amount}. You've exceeded your daily withdrawal limit {BankAccount.MAXIMAL_WITHDRAW}"

class OverdraftMaxException(Exception):
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"The amount of money you want to withdraw is {self.amount}. You've exceeded your balance."

class NegativeDepositException(Exception):
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Invalid deposit amount: {self.amount}. Deposit amount must be non-negative."
