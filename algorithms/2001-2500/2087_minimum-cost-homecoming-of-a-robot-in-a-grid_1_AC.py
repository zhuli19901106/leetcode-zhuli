# https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/
# this is trolling
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        sx, sy = startPos
        ex, ey = homePos

        res = 0

        d = +1 if sx < ex else -1
        for x in range(sx + d, ex + d, d):
            res += rowCosts[x]
        d = +1 if sy < ey else -1
        for y in range(sy + d, ey + d, d):
            res += colCosts[y]

        return res
