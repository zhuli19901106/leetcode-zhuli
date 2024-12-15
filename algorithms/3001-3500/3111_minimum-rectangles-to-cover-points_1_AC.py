# https://leetcode.com/problems/minimum-rectangles-to-cover-points/
# y doesn't matter at all
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        a = list(set([x for x, y in points]))
        a.sort()

        res = 0
        n = len(a)
        i = 0
        w += 1
        while i < n:
            j = i + 1
            while j < n and a[j] - a[i] < w:
                j += 1
            res += 1
            i = j
        return res
