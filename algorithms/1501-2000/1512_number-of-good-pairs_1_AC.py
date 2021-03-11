# https://leetcode.com/problems/number-of-good-pairs/
# 1AC
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        mm = {}
        for x in nums:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1
        res = 0
        for k, v in mm.items():
            res += v * (v - 1) // 2
        return res
