# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/
# 1AC
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res ^= x
        return res
