# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        inc_len, streak = 1, 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                streak += 1
                inc_len = max(inc_len, streak)
            else:
                streak = 1

        dec_len, streak = 1, 1
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                streak += 1
                dec_len = max(dec_len, streak)
            else:
                streak = 1

        return max(inc_len, dec_len)
