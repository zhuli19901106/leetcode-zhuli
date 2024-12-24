# easy
# https://leetcode.com/problems/find-the-highest-altitude/
# 1AC
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res, cur = 0, 0
        for x in gain:
            cur += x
            res = max(res, cur)
        return res
