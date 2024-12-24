# easy
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3289/
class Solution:
    def countElements(self, arr: List[int]) -> int:
        mm = {}
        for x in arr:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1
        res = 0
        for k, v in mm.items():
            if k + 1 in mm:
                res += v
        return res
