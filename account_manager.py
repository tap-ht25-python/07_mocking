
def calculate_interest(account):
    # account ska vara ett BankAccount
    before = account.get_balance()
    interest = 1.05
    after = before * interest
    account.set_balance(after)

# initial = account.get_balance()
# after_interest = initial * 1.05
# account.set_balance(after_interest)
