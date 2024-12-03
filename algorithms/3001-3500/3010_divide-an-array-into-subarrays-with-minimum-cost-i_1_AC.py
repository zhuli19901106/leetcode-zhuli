# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return nums[0] + sum(sorted(nums[1:])[:2])
