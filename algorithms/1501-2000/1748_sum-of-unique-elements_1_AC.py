# easy
# https://leetcode.com/problems/sum-of-unique-elements/
# 1AC
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        mm = {}
        for x in nums:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1
        res = 0
        for k, v in mm.items():
            if v == 1:
                res += k
        return res
