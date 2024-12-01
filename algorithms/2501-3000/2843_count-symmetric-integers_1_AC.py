# https://leetcode.com/problems/count-symmetric-integers/
from math import floor, log10

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high + 1):
            if self.isSymmetric(i):
                res += 1
        return res

    def isSymmetric(self, x):
        nd = int(floor(log10(x))) + 1
        if nd % 2 == 1:
            return False
        b10 = 10 ** (nd // 2)
        h1, h2 = x // b10, x % b10
        return self.sumDigits(h1) == self.sumDigits(h2)

    def sumDigits(self, x):
        sm = 0
        while x != 0:
            sm += x % 10
            x //= 10
        return sm
