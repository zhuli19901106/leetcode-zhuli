# https://leetcode.com/problems/maximum-difference-between-increasing-elements/
# 1AC

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return -1
        min_val = nums[0]

        res = -1
        for i in range(1, n):
            if nums[i] > min_val:
                res = max(res, nums[i] - min_val)
            else:
                min_val = min(min_val, nums[i])
        return res
