# easy
# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
# 1AC
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1] + 1:
                res += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1
        return res
