# medium
# https://leetcode.com/problems/interval-list-intersections/
# Runtime: 148 ms, faster than 96.28% of Python3 online submissions for Interval List Intersections.
# Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Interval List Intersections.
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a = A
        b = B
        na = len(a)
        nb = len(b)
        i = 0
        j = 0
        res = []
        while i < na and j < nb:
            x = max(a[i][0], b[j][0])
            y = min(a[i][1], b[j][1])
            if x <= y:
                res.append([x, y])
            if a[i][1] < b[j][1]:
                i += 1
            else:
                j += 1
        return res
