# easy
# https://leetcode.com/problems/largest-triangle-area/
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(ps):
            p1, p2, p3 = ps
            res = 0
            res += p2[0] * p3[1] - p3[0] * p2[1]
            res -= p1[0] * p3[1] - p3[0] * p1[1]
            res += p1[0] * p2[1] - p2[0] * p1[1]
            return abs(res / 2)

        ps = points
        n = len(ps)
        res = 0
        for i1 in range(n):
            for i2 in range(i1 + 1, n):
                for i3 in range(i2 + 1, n):
                    res = max(res, area([ps[i1], ps[i2], ps[i3]]))
        return res
