# easy
# https://leetcode.com/problems/harshad-number/
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sm = self.sumDigit(x)
        return sm if x % sm == 0 else -1

    def sumDigit(self, x):
        sm = 0
        while x != 0:
            sm += x % 10
            x //= 10
        return sm
