# medium
# https://leetcode.com/problems/remove-covered-intervals/
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        a = sorted(intervals, key=lambda x: (x[0], -x[1]))
        n = len(a)
        i = 0
        res = n
        while i + 1 < n:
            j = i + 1
            while j < n and a[i][0] <= a[j][0] and a[i][1] >= a[j][1]:
                j += 1
                res -= 1
            i = j
        return res
