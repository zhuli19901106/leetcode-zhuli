# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
# 1AC, simple idea and lots of manual labor
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def findRoot(m, x):
            if not x in m:
                m[x] = x
                return x
            r = x
            while r != m[r]:
                r = m[r]
            k = x
            while x != r:
                x = m[x]
                m[k] = r
                k = x
            return r

        # construct graph
        gr = {}
        gc = {}
        for p in stones:
            if not p[0] in gr:
                gr[p[0]] = []
            gr[p[0]].append(p[1])
            if not p[1] in gc:
                gc[p[1]] = []
            gc[p[1]].append(p[0])

        # use disjoint set to calculate connected component
        R = 10001
        ds = {}
        for x in gr:
            y0 = gr[x][0]
            for y in gr[x]:
                p1 = x * R + y0
                p2 = x * R + y
                r1 = findRoot(ds, p1)
                r2 = findRoot(ds, p2)
                if r1 == r2:
                    continue
                ds[r1] = r2
        for y in gc:
            x0 = gc[y][0]
            for x in gc[y]:
                p1 = x0 * R + y
                p2 = x * R + y
                r1 = findRoot(ds, p1)
                r2 = findRoot(ds, p2)
                if r1 == r2:
                    continue
                ds[r1] = r2

        # count roots
        rs = set()
        for x in ds:
            rs.add(findRoot(ds, x))
        return len(stones) - len(rs)
