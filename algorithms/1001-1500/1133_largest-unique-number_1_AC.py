# easy
# https://leetcode.com/problems/largest-unique-number/
# 1AC
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        res = None
        mm = {}
        for x in A:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1
        for k, v in mm.items():
            if v == 1:
                res = k if res is None else max(res, k)
        return -1 if res is None else res
