# medium
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
# 1AC, disjoint set
class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        ds = {}

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

        n = len(A)
        for i in range(n):
            x, y = A[i], B[i]
            rx = findRoot(ds, x)
            ry = findRoot(ds, y)
            if rx < ry:
                ds[ry] = rx
            elif rx > ry:
                ds[rx] = ry
        return ''.join([findRoot(ds, c) for c in S])
