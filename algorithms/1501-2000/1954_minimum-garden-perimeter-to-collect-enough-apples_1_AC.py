# medium
# https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/
# this is pure math
from math import ceil, sqrt

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        ll = 0
        rr = int(1e10)
        while rr - ll > 1:
            mm = ll + (rr - ll >> 1)
            sm = 2 * mm * (mm + 1) * (2 * mm + 1)
            if sm < neededApples:
                ll = mm
            else:
                rr = mm

        res = 8 * rr
        return res
