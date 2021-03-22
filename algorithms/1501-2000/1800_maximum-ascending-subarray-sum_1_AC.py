# https://leetcode.com/problems/maximum-ascending-subarray-sum/
# 1AC
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        max_sum = 0
        while i < n:
            j = i + 1
            while j < n and nums[j - 1] < nums[j]:
                j += 1
            cur_sum = 0
            while i < j:
                cur_sum += nums[i]
                i += 1
            max_sum = max(max_sum, cur_sum)
        return max_sum
