# medium
# https://leetcode.com/problems/sequential-digits/
# precompute and bisect
from bisect import bisect_left, bisect_right

class Solution:
    def __init__(self):
        res = []
        a = list(range(1, 10))
        res += a
        while True:
            a1 = []
            for x in a:
                d = x % 10
                if d < 9:
                    a1.append(x * 10 + (d + 1))
            if len(a1) == 0:
                break
            res += a1
            a = a1
        self.res = res

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = self.res
        i1 = bisect_left(res, low)
        i2 = bisect_right(res, high)
        return res[i1: i2]
