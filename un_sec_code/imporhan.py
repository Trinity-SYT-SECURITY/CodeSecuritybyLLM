import logging


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient funds")
            self.balance -= amount
        except Exception as e:
            logging.error(str(e))


account = BankAccount(100)
account.withdraw(200)
# In Python, improper handling of exceptions may lead to security vulnerabilities, such as leaking sensitive information through error messages.
