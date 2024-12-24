# easy
# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
# 1AC
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sm = sm = 0
        for x in nums:
            sm += x
            min_sm = min(min_sm, sm)
        res = 1 - min(0, min_sm)
        return res
