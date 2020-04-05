# https://leetcode.com/problems/count-largest-group/
# 1AC
class Solution:
    def __init__(self):
        MAXN = 10000
        ds = [0 for i in range(MAXN + 1)]
        for i in range(1, MAXN + 1):
            v = 0
            j = i
            while j > 0:
                v += j % 10
                j //= 10
            ds[i] = v
        self.ds = ds

    def countLargestGroup(self, n: int) -> int:
        mm = {}
        mv = 0
        for i in range(1, n + 1):
            v = self.ds[i]
            mm[v] = mm.get(v, 0) + 1
            mv = max(mv, mm[v])
        res = 0
        for v in mm.values():
            if v == mv:
                res += 1
        return res
