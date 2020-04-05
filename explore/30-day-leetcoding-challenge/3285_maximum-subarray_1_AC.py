# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3285/
# 1AC
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        if res <= 0:
            return res
        res = sm = 0
        for x in nums:
            sm += x
            res = max(res, sm)
            sm = max(sm, 0)
        return res
