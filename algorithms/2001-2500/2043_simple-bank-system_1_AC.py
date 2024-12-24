# medium
# https://leetcode.com/problems/simple-bank-system/
class Bank:

    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.bs = balance[:]

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account1 > self.n:
            return False
        if account2 < 1 or account2 > self.n:
            return False
        if self.bs[account1 - 1] < money:
            return False

        self.bs[account1 - 1] -= money
        self.bs[account2 - 1] += money

        return True

    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n:
            return False

        self.bs[account - 1] += money

        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n:
            return False
        if self.bs[account - 1] < money:
            return False

        self.bs[account - 1] -= money

        return True        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)