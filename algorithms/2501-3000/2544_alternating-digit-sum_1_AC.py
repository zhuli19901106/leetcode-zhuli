# https://leetcode.com/problems/alternating-digit-sum/
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        odd = True
        sm = 0
        while n != 0:
            d = n % 10
            n //= 10
            sm += d if odd else -d
            odd = not odd
        return -sm if odd else sm
