class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = dict(zip(range(1, len(balance) + 1), balance))
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.accounts and account2 in self.accounts:
            if money <= self.accounts[account1]:
                self.accounts[account2] += money
                self.accounts[account1] -= money
                return True
        return False
        

    def deposit(self, account: int, money: int) -> bool:
        if account not in self.accounts: return False
        self.accounts[account] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if account not in self.accounts or money > self.accounts[account]: return False
        self.accounts[account] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)