# medium
# https://leetcode.com/problems/satisfiability-of-equality-equations/
# 1AC, disjoint set
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
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
        qs = []
        for s in equations:
            x, y = s[0], s[3]
            sg = s[1:3]
            if sg == '==':
                rx = findRoot(ds, x)
                ry = findRoot(ds, y)
                if rx != ry:
                    ds[rx] = ry
            else:
                qs.append((x, y))
        for x, y in qs:
            rx = findRoot(ds, x)
            ry = findRoot(ds, y)
            if rx == ry:
                return False
        return True
