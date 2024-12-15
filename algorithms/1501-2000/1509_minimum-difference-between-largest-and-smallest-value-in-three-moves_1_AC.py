# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
# sort of a teaser
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0

        nums.sort()
        res = min(nums[n - 2] - nums[2], nums[n - 3] - nums[1])
        res = min(res, nums[n - 4] - nums[0], nums[n - 1] - nums[3])
        return res
