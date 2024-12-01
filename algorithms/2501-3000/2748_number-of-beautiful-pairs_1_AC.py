# https://leetcode.com/problems/number-of-beautiful-pairs/
from math import floor, log10

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if self.isBeautiful(nums[i], nums[j]):
                    res += 1
        return res

    def isBeautiful(self, x, y):
        return self.coprime(x // 10 ** floor(log10(x)), y % 10)

    def coprime(self, x, y):
        return self.gcd(x, y) == 1

    def gcd(self, x, y):
        if x > y:
            x, y = y, x
        while x != 0:
            x, y = y % x, x
        return y
