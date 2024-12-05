# https://leetcode.com/problems/find-the-key-of-the-numbers/
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        res = 0
        b10 = 1
        for i in range(4):
            d1, d2, d3 = num1 % 10, num2 % 10, num3 % 10
            num1 //= 10
            num2 //= 10
            num3 //= 10
            res += b10 * min(d1, d2, d3)
            b10 *= 10
        return res
