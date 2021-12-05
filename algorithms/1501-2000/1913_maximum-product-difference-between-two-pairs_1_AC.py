# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
# 1AC, all positive

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a = sorted(nums)
        return a[-1] * a[-2] - a[0] * a[1]
