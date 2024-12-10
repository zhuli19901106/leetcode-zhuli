# https://leetcode.com/problems/count-the-number-of-complete-components/
# simple but verbose
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        deg = [0 for i in range(n)]
        dj = [i for i in range(n)]
        for x, y in edges:
            deg[x] += 1
            deg[y] += 1
            rx = self.findRoot(dj, x)
            ry = self.findRoot(dj, y)
            dj[rx] = ry

        mm = {}
        for x in range(n):
            r = self.findRoot(dj, x)
            if not r in mm:
                mm[r] = []
            mm[r].append(x)

        res = 0
        for xs in mm.values():
            nx = len(xs)
            complete = True
            for x in xs:
                if deg[x] != nx - 1:
                    complete = False
                    break
            if complete:
                res += 1

        return res

    def findRoot(self, dj, x):
        r = x
        while dj[r] != r:
            r = dj[r]

        k = x
        while x != r:
            x = dj[x]
            dj[k] = r
            k = x
        return r
