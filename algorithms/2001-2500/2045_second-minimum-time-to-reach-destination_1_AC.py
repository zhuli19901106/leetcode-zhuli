# hard
# https://leetcode.com/problems/second-minimum-time-to-reach-destination/
# you can traverse the graph forever
# but you won't because it's already taking too long
# don't use DFS
from heapq import heappush, heappop

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        if n == 1:
            return 0

        g = {}
        for x in range(1, n + 1):
            g[x] = set()
        for x, y in edges:
            g[x].add(y)
            g[y].add(x)

        sx, ex = 1, n
        res = {}
        for i in range(1, n + 1):
            res[i] = set()

        pq = []

        res[sx].add(0)
        heappush(pq, (0, sx))
        while len(res[ex]) < 2:
            cur_time, x = heappop(pq)

            for y in g[x]:
                # wait for red light
                nc = cur_time // change
                wait_time = (change - cur_time % change) if nc % 2 == 1 else 0
                next_time = cur_time + wait_time + time

                # important pruning
                if len(res[y]) >= 2:
                    continue

                res[y].add(next_time)
                heappush(pq, (cur_time + wait_time + time, y))

        return max(res[ex])
