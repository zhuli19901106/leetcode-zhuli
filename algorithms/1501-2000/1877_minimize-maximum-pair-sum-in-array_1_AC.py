# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
# 1AC, sort it

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        a = sorted(nums)
        n = len(a)

        i = 0
        res = 0
        while i < n - 1 - i:
            res = max(res, a[i] + a[n - 1 - i])
            i += 1
        return res
