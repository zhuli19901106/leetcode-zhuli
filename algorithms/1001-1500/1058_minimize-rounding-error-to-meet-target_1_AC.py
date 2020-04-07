# https://leetcode.com/problems/minimize-rounding-error-to-meet-target/
# normalize, sort and scan
from math import floor

class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        p = [float(s) for s in prices]
        p1 = []
        for x in p:
            fx = floor(x)
            if x == fx:
                target -= fx
            else:
                p1.append(x - fx)
                target -= fx
        p = p1
        n = len(p)
        if target < 0 or target > n:
            return str(-1)

        p.sort()
        i = n - 1
        cur = 0
        res = sum(p)
        while cur < target:
            res += 1 - 2 * p[i]
            cur += 1
            i -= 1
        return '{:.3f}'.format(res)
