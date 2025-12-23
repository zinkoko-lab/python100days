# level-5: Encapsulation

# Encapsulating data using private variables


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance  # Private Variable

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
print(account.get_balance())
# print(account.__balance) -> AttributeError: 'BankAccount' object has no attribute '__balance'.
