# https://leetcode.com/problems/maximal-network-rank/
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        mm_deg = {}

        for x, y in roads:
            if not x in mm_deg:
                mm_deg[x] = set()
            mm_deg[x].add(y)

            if not y in mm_deg:
                mm_deg[y] = set()
            mm_deg[y].add(x)

        res = 0
        for x in range(n):
            for y in range(x + 1, n):
                cur = 0
                cur += len(mm_deg[x]) if x in mm_deg else 0
                cur += len(mm_deg[y]) if y in mm_deg else 0
                cur -= (1 if y in mm_deg and x in mm_deg[y] else 0)
                res = max(res, cur)

        return res
