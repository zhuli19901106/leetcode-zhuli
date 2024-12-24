# hard
# https://leetcode.com/problems/employee-free-time/
# invert and do an iterative intersection of intervals
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        INT_MAX = 2 ** 63 - 1
        INT_MIN = INT_MAX
        for sc in schedule:
            INT_MIN = min(INT_MIN, sc[0].start)

        # convert to free intervals
        def convertFree(sc):
            res = []
            x = INT_MIN
            for it in sc:
                if x < it.start:
                    res.append([x, it.start])
                x = it.end
            res.append([x, INT_MAX])
            return res

        # intersection of intervals
        def intersect(a, b):
            na = len(a)
            nb = len(b)
            i = 0
            j = 0
            res = []
            while i < na and j < nb:
                x = max(a[i][0], b[j][0])
                y = min(a[i][1], b[j][1])
                if x < y:
                    res.append([x, y])
                if a[i][1] < b[j][1]:
                    i += 1
                else:
                    j += 1
            return res

        sc1 = [[0, INT_MAX]]
        for sc in schedule:
            sc2 = convertFree(sc)
            sc3 = intersect(sc1, sc2)
            sc2 = sc3
            sc1 = sc2
        sc3.pop()
        res = []
        for x, y in sc3:
            res.append(Interval(x, y))
        return res
