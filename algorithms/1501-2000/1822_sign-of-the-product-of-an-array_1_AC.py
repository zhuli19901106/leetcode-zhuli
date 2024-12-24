# easy
# https://leetcode.com/problems/sign-of-the-product-of-an-array/
# 1AC
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for x in nums:
            sig = 1 if x > 0 else -1 if x < 0 else 0
            res *= sig
        return res
