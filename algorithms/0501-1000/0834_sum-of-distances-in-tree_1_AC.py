# hard
# https://leetcode.com/problems/sum-of-distances-in-tree/
# tricky, but still manageable
# took me long enough, this is tough
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = {}
        for x in range(n):
            g[x] = set()
        for x, y in edges:
            g[x].add(y)
            g[y].add(x)

        vst = set()
        mm = {}
        for x in range(n):
            mm[x] = 1

        res = [0 for i in range(n)]
        sx = 0

        vst.clear()
        self.searchAll(-1, sx, g, vst, mm, res)

        vst.clear()
        self.searchOnceMore(sx, g, vst, mm, res)

        return res

    def searchAll(self, last_x, x, g, vst, mm, res):
        vst.add(x)

        n = len(g)
        for y in g[x]:
            if y in vst:
                continue

            self.searchAll(x, y, g, vst, mm, res)

            # how do people come up with this?
            mm[x] += mm[y]
            res[x] += res[y] + mm[y]

    def searchOnceMore(self, x, g, vst, mm, res):
        vst.add(x)

        n = len(g)

        for y in g[x]:
            if y in vst:
                continue

            # now to get res[y] from res[x]
            res[y] = res[x] + (n - mm[y]) - mm[y]

            self.searchOnceMore(y, g, vst, mm, res)
