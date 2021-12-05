# https://leetcode.com/problems/find-greatest-common-divisor-of-array/
# 1AC

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x1, x2 = min(nums), max(nums)
        return self.gcd(x1, x2)

    def gcd(self, x, y):
        if x > y:
            return self.gcd(y, x)
        while x != 0:
            x, y = y % x, x
        return y
