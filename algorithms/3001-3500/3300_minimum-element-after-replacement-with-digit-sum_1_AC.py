# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min([self.sumDigits(x) for x in nums])

    def sumDigits(self, x):
        res = 0
        while x != 0:
            res += x % 10
            x //= 10
        return res
