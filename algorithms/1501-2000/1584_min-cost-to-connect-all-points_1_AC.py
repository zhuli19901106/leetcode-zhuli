# https://leetcode.com/problems/min-cost-to-connect-all-points/
# mst problem

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        edges.sort()

        def findRoot(dj, x):
            r = x
            while r != dj[r]:
                r = dj[r]
            k = x
            while x != r:
                x = dj[x]
                dj[k] = r
                k = x

            return r

        dj = [i for i in range(n)]

        res = 0
        cc = 0
        for dist, x, y in edges:
            if cc >= n - 1:
                break
            rx = findRoot(dj, x)
            ry = findRoot(dj, y)
            if rx == ry:
                continue
            dj[rx] = ry
            cc += 1
            res += dist

        return res
