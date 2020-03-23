# https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/
# 1AC, boring
class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        def sumDigit(x):
            res = 0
            while x != 0:
                res += x % 10
                x //= 10
            return res

        return 1 - sumDigit(min(A)) % 2
