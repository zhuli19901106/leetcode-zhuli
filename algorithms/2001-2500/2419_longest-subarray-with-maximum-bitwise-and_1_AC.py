# medium
# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/
# this is a teaser, once you get it
# if the subarray contains more than 1 unique value, why not pick the largest one alone
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_val, max_len = 0, 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            if (nums[i], j - i) > (max_val, max_len):
                max_val, max_len = nums[i], j - i
            i = j

        return max_len
