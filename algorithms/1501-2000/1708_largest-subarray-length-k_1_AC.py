# easy
# https://leetcode.com/problems/largest-subarray-length-k/
# 1AC, the trick is about distinctness

class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_i = 0
        for i in range(n - k + 1):
            if nums[i] > nums[max_i]:
                max_i = i
        return nums[max_i: max_i + k]
