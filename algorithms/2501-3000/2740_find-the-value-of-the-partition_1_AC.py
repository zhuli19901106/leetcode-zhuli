# https://leetcode.com/problems/find-the-value-of-the-partition/
# should be "easy"
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        res = nums[-1] - nums[0]
        n = len(nums)

        for i in range(n - 1):
            res = min(res, nums[i + 1] - nums[i])
        return res
