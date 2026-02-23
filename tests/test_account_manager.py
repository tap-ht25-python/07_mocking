from bank_account import BankAccount


def test_calculate_interest():
    # arrange
    account = BankAccount()
    initial = account.get_balance()
    after_interest = initial * 1.05

    # act
    calculate_interest(account)

    # assert
    actual = account.get_balance()
    assert actual == after_interest

