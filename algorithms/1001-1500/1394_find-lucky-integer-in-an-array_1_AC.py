# https://leetcode.com/problems/find-lucky-integer-in-an-array/
# 1AC
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mm = {}
        for x in arr:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1
        res = None
        for x in mm:
            if mm[x] != x:
                continue
            if res is None or res < x:
                res = x
        return res if res else -1
