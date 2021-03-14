# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# 1AC, pointless
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = sorted(nums)
        return (a[-1] - 1) * (a[-2] - 1)
