# medium
# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/
# 1AC, disjoint set
class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        def findRoot(ds, x):
            if not x in ds:
                ds[x] = x
            r = x
            while r != ds[r]:
                r = ds[r]
            k = x
            while x != r:
                x = ds[x]
                ds[k] = r
                k = x
            return r

        logs.sort(key=lambda x: x[0])
        cc = N
        ds = {}
        for ts, x, y in logs:
            rx = findRoot(ds, x)
            ry = findRoot(ds, y)
            if rx == ry:
                continue
            ds[rx] = ry
            cc -= 1
            if cc == 1:
                return ts
        return -1
