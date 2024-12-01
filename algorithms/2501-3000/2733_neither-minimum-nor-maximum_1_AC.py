# https://leetcode.com/problems/neither-minimum-nor-maximum/
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)
        for x in nums:
            if x != min_val and x != max_val:
                return x
        return -1
