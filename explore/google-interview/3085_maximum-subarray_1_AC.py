# https://leetcode.com/explore/interview/card/google/64/dynamic-programming-4/3085/
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
