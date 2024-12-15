# https://leetcode.com/problems/two-best-non-overlapping-events/
# careful, at most 2, not exactly 2
from bisect import bisect_right

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)

        # max values of right suffix
        mvs = [0 for i in range(n)]
        mv = 0
        for i in range(n - 1, -1, -1):
            mv = max(mv, events[i][2])
            mvs[i] = mv

        xs = [x for x, y, v in events]
        # at most 2, could be 1
        res = mvs[0]
        n = len(events)
        for i in range(n - 1):
            y = events[i][1]
            j = bisect_right(xs, y, i + 1)
            if j >= n:
                continue
            res = max(res, events[i][2] + mvs[j])

        return res
