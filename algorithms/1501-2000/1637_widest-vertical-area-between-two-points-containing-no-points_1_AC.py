# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
# 1AC, seriously?

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        a = sorted([x for x, y in points])
        n = len(a)
        res = a[1] - a[0]
        for i in range(n - 1):
            res = max(res, a[i + 1] - a[i])
        return res
