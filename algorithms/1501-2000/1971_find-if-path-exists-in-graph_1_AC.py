# easy
# https://leetcode.com/problems/find-if-path-exists-in-graph/
# 1AC, disjoint set

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        dj = [i for i in range(n)]
        for x, y in edges:
            rx, ry = self.findRoot(dj, x), self.findRoot(dj, y)
            if rx != ry:
                dj[rx] = ry

        rst, ren = self.findRoot(dj, start), self.findRoot(dj, end)
        return rst == ren

    def findRoot(self, dj, x):
        r = x
        while dj[r] != r:
            r = dj[r]
        k = x
        while x != r:
            x = dj[k]
            dj[k] = r
            k = x
        return r
