# easy
# https://leetcode.com/problems/number-of-common-factors/
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        x = self.gcd(a, b)
        res = 0
        i = 1
        while i <= x // i:
            if x % i == 0:
                res += 2
            if i * i == x:
                res -= 1
            i += 1

        return res

    def gcd(self, x, y):
        if x < y:
            return self.gcd(y, x)
        while y != 0:
            x, y = y, x % y
        return x
