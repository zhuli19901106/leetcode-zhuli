# medium
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def findRoot(ds, x):
            if not x in ds:
                ds[x] = x
                return x
            r = x
            while r != ds[r]:
                r = ds[r]
            k = x
            while x != r:
                x = ds[x]
                ds[k] = r
                k = x
            return r

        ds = {}
        for i in range(n):
            ds[i] = i
        num_extra = 0
        for x, y in connections:
            rx = findRoot(ds, x)
            ry = findRoot(ds, y)
            if rx == ry:
                num_extra += 1
            else:
                ds[rx] = ry
        for x in ds:
            findRoot(ds, x)
        num_cc = len(set(ds.values()))

        return num_cc - 1 if num_extra >= num_cc - 1 else -1
