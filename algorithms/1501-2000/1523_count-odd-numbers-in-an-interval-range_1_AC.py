# easy
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
# well, can't be to caught off guard
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = (high - low + 1) // 2
        if (high & 1) and (low & 1):
            res += 1
        return res
