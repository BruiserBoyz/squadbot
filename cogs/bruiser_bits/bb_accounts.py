class MemberAccount:
    def __init__(self):
        self.account_owner = ""
        self.account_balance = 0.00

    def set_balance(self, amount):
        self.account_balance += amount

    def set_owner(self, new_owner):
        self.account_owner = new_owner

    def get_balance(self):
        return self.account_balance

    def get_owner(self):
        return self.account_owner
