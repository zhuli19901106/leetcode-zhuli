# https://leetcode.com/problems/smallest-string-with-swaps/
# 1AC, the idea of connected component is rather tricky
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
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

        n = len(s)
        ds = [i for i in range(n)]
        for x, y in pairs:
            rx = findRoot(ds, x)
            ry = findRoot(ds, y)
            if rx == ry:
                continue
            ds[rx] = ry

        mm = {}
        for i in range(n):
            findRoot(ds, i)
            if not ds[i] in mm:
                mm[ds[i]] = [[], []]
            mm[ds[i]][0].append(s[i])
            mm[ds[i]][1].append(i)

        res = [0 for i in range(n)]
        for v in mm.values():
            v[0].sort()
            v[1].sort()
            nv = len(v[0])
            for i in range(nv):
                res[v[1][i]] = v[0][i]

        return ''.join(res)
