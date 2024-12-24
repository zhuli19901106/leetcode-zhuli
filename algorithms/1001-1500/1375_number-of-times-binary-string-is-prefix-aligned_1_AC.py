# medium
# https://leetcode.com/problems/bulb-switcher-iii/
# 1AC, use Fenwick tree to record prefix sum
# this problem can be solved with tree map by recording intervals
class BIT:
    def __init__(self, n):
        self.a = [0 for i in range(n + 1)]
        self.n = n

    def add(self, idx, val):
        a = self.a
        n = self.n
        if idx < 1 or idx > n:
            return
        i = idx
        while i <= n:
            a[i] += val
            i += (i & -i)

    def sum(self, idx):
        if idx < 1:
            return 0
        a = self.a
        n = self.n
        idx = min(idx, n)

        res = 0
        i = idx
        while i > 0:
            res += a[i]
            i -= (i & -i)
        return res

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        bit = BIT(n)
        res = 0
        for x in light:
            bit.add(x, 1)
            sm = bit.sum(n)
            if bit.sum(sm) == sm:
                res += 1
        return res
