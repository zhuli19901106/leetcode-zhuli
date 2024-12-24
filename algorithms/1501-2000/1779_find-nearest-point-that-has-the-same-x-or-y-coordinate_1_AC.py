# easy
# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
# 1AC
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mi = -1
        md = 0
        for i, p in enumerate(points):
            x1, y1 = p
            if not (x1 == x or y1 == y):
                continue
            d = abs(x1 - x) + abs(y1 - y)
            if mi == -1 or d < md:
                mi, md = i, d
        return mi
