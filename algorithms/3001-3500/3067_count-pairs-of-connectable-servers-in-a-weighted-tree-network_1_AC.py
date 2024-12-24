# medium
# https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/
# a lot of trouble for one medium problem
# this is ridiculous
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        g = {}
        n = 0
        for x, y, d in edges:
            if not x in g:
                g[x] = {}
            if not y in g:
                g[y] = {}
            g[x][y] = d
            g[y][x] = d
            n = max(n, x + 1)
            n = max(n, y + 1)

        res = []
        for i in range(n):
            res.append(self.countConnectable(i, g, signalSpeed))
        return res

    def countConnectable(self, x, g, signalSpeed):
        if not x in g:
            return 0

        ac = []
        for y in g[x]:
            vst = set()
            dist = {}

            vst.add(x)
            self.traverse(y, g[x][y], g, vst, dist)

            cc = len([d for d in dist.values() if d % signalSpeed == 0])
            if cc > 0:
                ac.append(cc)

        m = len(ac)
        res = 0
        suf = 0
        for i in range(m - 1, -1, -1):
            res += ac[i] * suf
            suf += ac[i]
        return res

    def traverse(self, x, d, g, vst, dist):
        if x in vst:
            return
        vst.add(x)
        dist[x] = d
        for y in g[x]:
            if y in vst:
                continue
            self.traverse(y, d + g[x][y], g, vst, dist)
