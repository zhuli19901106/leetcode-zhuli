# https://leetcode.com/problems/smallest-divisible-digit-product-i/
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if self.productDigits(n) % t == 0:
                break
            n += 1
        return n

    def productDigits(self, x):
        if x == 0:
            return 0
        res = 1
        while x != 0 and res != 0:
            res *= x % 10
            x //= 10
        return res
