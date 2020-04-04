# https://leetcode.com/problems/connecting-cities-with-minimum-cost/
# 1AC, MST problem
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        def findRoot(ds, x):
            r = x
            while r != ds[r]:
                r = ds[r]
            k = x
            while x != r:
                x = ds[x]
                ds[k] = r
                k = x
            return r

        cs = connections
        cs.sort(key=lambda x: x[2])
        ds = [i for i in range(N + 1)]
        cc = N
        res = 0
        for x, y, d in cs:
            rx = findRoot(ds, x)
            ry = findRoot(ds, y)
            if rx == ry:
                continue
            ds[rx] = ry
            cc -= 1
            res += d
            if cc == 1:
                break
        return res if cc == 1 else -1
