# easy
# https://leetcode.com/problems/sum-multiples/
class Solution:
    def __init__(self):
        self.MAXN = 1000
        self.res = [0 for i in range(self.MAXN + 1)]
        for i in range(1, self.MAXN + 1):
            self.res[i] = self.res[i - 1]
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                self.res[i] += i

    def sumOfMultiples(self, n: int) -> int:
        return self.res[n]
