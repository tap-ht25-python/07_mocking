#from bank_account import BankAccount
from account_manager import calculate_interest


def test_calculate_interest():
    # arrange
    account = FakeAccount()
    initial = account.balance
    after_interest = initial * 1.05

    # act
    calculate_interest(account)

    # assert
    actual = account.balance
    assert actual == after_interest


class FakeAccount:
    def __init__(self):
        self.balance = 2000   # 5% är 100 kr

    def get_balance(self):
        return self.balance

    def set_balance(self, new_balance):
        self.balance = new_balance


# Exempel på hur en Mock class kan se ut - men i vanliga fall skapar man denna av ett testramverk
class MockAccount:
    def __init__(self):
        self.num_calls = 0
        self.args = []

    def set_balance(self, new_balance):
        self.num_calls += 1
        self.args.append(new_balance)

# i testfallet:  (balance 2000)
# - num_calls == 1
# - args == [2100]
