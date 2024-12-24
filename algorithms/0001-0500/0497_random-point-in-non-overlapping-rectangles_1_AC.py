# medium
# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
# two fold random
from bisect import bisect_left
from random import randint

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        n = len(rects)
        self.n = n

        areas = []
        areas_ps = []
        ps = 0
        for x1, y1, x2, y2 in rects:
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            ar = (x2 - x1 + 1) * (y2 - y1 + 1)
            ps += ar
            areas_ps.append(ps)
        self.areas = areas
        self.areas_ps = areas_ps

    def pick(self) -> List[int]:
        areas_ps = self.areas_ps
        rects = self.rects
        n = self.n

        idx = bisect_left(areas_ps, randint(0, areas_ps[-1]))
        idx = min(idx, n - 1)
        x1, y1, x2, y2 = rects[idx]

        if x1 > x2:
            x1, x2 = x2, x1
        x = randint(x1, x2)

        if y1 > y2:
            y1, y2 = y2, y1
        y = randint(y1, y2)

        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()