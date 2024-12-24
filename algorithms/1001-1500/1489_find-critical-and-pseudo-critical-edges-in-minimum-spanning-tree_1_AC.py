# hard
# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
# maybe just BF
# even without caring about efficiency, this problem is still tricky enough
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ae = [(e[2], e[0], e[1], i) for i, e in enumerate(edges)]
        ae.sort()

        sm0 = self.calcMST(n, ae)

        ne = len(ae)
        crit, pseu_crit = [], []
        for i in range(ne):
            sm = self.calcMST(n, ae, -1, i)
            if sm == -1 or sm > sm0:
                crit.append(ae[i][3])
                continue

            sm = self.calcMST(n, ae, i, -1)
            if sm == sm0:
                pseu_crit.append(ae[i][3])
        return [crit, pseu_crit]

    def calcMST(self, n, ae, i_use=-1, i_skip=-1):
        dj = dict([(i, i) for i in range(n)])
        sm = 0

        if i_use != -1:
            w, x, y, idx = ae[i_use]
            rx = self.findRoot(dj, x)
            ry = self.findRoot(dj, y)
            dj[rx] = ry
            sm += w

        ne = len(ae)
        for i in range(ne):
            if i_skip != -1 and i == i_skip:
                continue

            w, x, y, idx = ae[i]
            rx = self.findRoot(dj, x)
            ry = self.findRoot(dj, y)
            if rx == ry:
                continue
            dj[rx] = ry
            sm += w

        roots = set([self.findRoot(dj, i) for i in range(n)])
        if len(roots) != 1:
            return -1
        return sm

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
