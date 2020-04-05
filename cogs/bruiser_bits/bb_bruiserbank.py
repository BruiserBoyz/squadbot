class BruiserBank:
    def __init__(self):
        self.total_balance = 0.00
        self.accounts_array = []

    def add_account(self, account_to_add):
        self.accounts_array.append(account_to_add)

    def delete_account(self):
        pass

    def set_balance(self, amount):
        self.total_balance += amount

    def get_all_accounts(self):
        return self.accounts_array.copy()

    def get_number_accounts(self):
        return len(self.accounts_array)

    def deposit(self, account, amount):
        self.accounts_array[account].set_balance(amount)

    def withdraw(self, account, amount):
        self.accounts_array[account].set_balance(-amount)

    def transfer(self, account_from, account_to, amount):
        self.accounts_array[account_from].set_balance(-amount)
        self.accounts_array[account_to].set_balance(amount)
