# medium
# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/
# wait, why is it remainder?
class Solution:
    def __init__(self):
        f1, f2 = 1, 2
        self.mm = {0: 0, f1: 1, f2: 1}
        self.fib = [f1, f2]

        MAX_N = 10 ** 9
        while True:
            f3 = f1 + f2
            if f3 > MAX_N:
                break
            self.mm[f3] = 1
            self.fib.append(f3)
            f1, f2 = f2, f3
        # absolutely necessary
        self.fib = self.fib[::-1]

    def findMinFibonacciNumbers(self, k: int) -> int:
        return self.dfs(k)

    def dfs(self, n):
        if n in self.mm:
            return self.mm[n]
        res = n
        for x in self.fib:
            if x > n:
                continue
            res = n // x + self.dfs(n % x)
            break
        self.mm[n] = res
        return res
