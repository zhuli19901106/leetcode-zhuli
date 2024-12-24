# easy
# https://leetcode.com/problems/running-sum-of-1d-array/
# 1AC
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cs = 0
        res = []
        for x in nums:
            cs += x
            res.append(cs)
        return res
