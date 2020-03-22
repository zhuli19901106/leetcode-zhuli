# https://leetcode.com/problems/sort-integers-by-the-power-value/
# 1AC, DFS with memorization
# https://en.wikipedia.org/wiki/Collatz_conjecture
class Solution:
    def __init__(self):
        self.mp = {0: 0, 1: 0}

    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = [(self.calcPower(i), i) for i in range(lo, hi + 1)]
        res.sort()
        return res[k - 1][1]

    def calcPower(self, x):
        mp = self.mp
        if x in mp:
            return mp[x]

        if x % 2 == 0:
            res = self.calcPower(x // 2) + 1
        else:
            res = self.calcPower(3 * x + 1) + 1
        mp[x] = res
        return res
