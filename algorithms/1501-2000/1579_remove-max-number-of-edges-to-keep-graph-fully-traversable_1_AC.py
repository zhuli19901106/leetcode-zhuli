# hard
# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
# knowing 1-cut algorithm is probably beyond the need for an average software engineer
# but it can be solved using union find, much simpler
# if union() actually detects two component (and joins them), that edge must be a cut
# honestly, I couldn't come up with this without taking hints
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        res = 0

        dj = {}
        for i in range(1, n + 1):
            dj[i] = i
        for ty, x, y in edges:
            if ty == 3 and not self.union(dj, x, y):
                res += 1

        dja = dj.copy()
        for ty, x, y in edges:
            if ty == 1 and not self.union(dja, x, y):
                res += 1

        djb = dj.copy()
        for ty, x, y in edges:
            if ty == 2 and not self.union(djb, x, y):
                res += 1

        ra = set([self.find(dja, i) for i in range(1, n + 1)])
        if len(ra) > 1:
            return -1

        rb = set([self.find(djb, i) for i in range(1, n + 1)])
        if len(rb) > 1:
            return -1

        return res

    def find(self, dj, x):
        r = x
        while dj[r] != r:
            r = dj[r]
        k = x
        while x != r:
            x = dj[x]
            dj[k] = r
            k = x
        return r

    def union(self, dj, x, y):
        rx = self.find(dj, x)
        ry = self.find(dj, y)
        dj[rx] = ry

        return rx != ry
