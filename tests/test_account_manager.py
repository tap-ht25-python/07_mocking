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

    def set_balance(self, new_balance):
        self.balance = new_balance
