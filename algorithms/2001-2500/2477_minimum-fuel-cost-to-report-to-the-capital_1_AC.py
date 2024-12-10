# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
# this should be "hard", at least a hard medium
# I paused for 30 minutes and finally came up with some weird post-order DFS BS
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        g = {}
        for x, y in roads:
            if not x in g:
                g[x] = set()
            if not y in g:
                g[y] = set()
            g[x].add(y)
            g[y].add(x)
        res = [0]
        vst = set()

        vst.add(0)
        self.dfs(g, 0, vst, seats, res)

        return res[0]

    def dfs(self, g, x, vst, seats, res):
        if not x in g:
            return 0

        sm_cc = 1
        for y in g[x]:
            if y in vst:
                continue
            vst.add(y)
            cc = self.dfs(g, y, vst, seats, res)
            sm_cc += cc

            # key here, don't care how the seats are allocated
            # only care how many cars needed
            # don't put this at the end of DFS
            res[0] += (cc + seats - 1) // seats

        return sm_cc
