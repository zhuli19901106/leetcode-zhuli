# https://leetcode.com/problems/the-time-when-the-network-becomes-idle/
# the description is insanely long, summary like this:
# - all edges weigh 1
# - data send to master and await reply
# - keep waiting patience[i] seconds and resend, unless already replied
# - how long it takes for all to be done
# because there's no concept of congestion and limit
# no interference between nodes exists
from collections import deque

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # build graph
        g = {}
        for x, y in edges:
            if not x in g:
                g[x] = set()
            if not y in g:
                g[y] = set()
            g[x].add(y)
            g[y].add(x)

        # search for shortest distance to all data nodes
        dist = {}
        q = deque()

        dist[0] = 0
        q.appendleft((0, 0))
        while len(q) > 0:
            x, d = q.pop()
            for y in g[x]:
                if y in dist:
                    continue
                dist[y] = d + 1
                q.appendleft((y, d + 1))

        # check idle time for each data node
        res = 0
        for x, d in dist.items():
            if x == 0:
                continue

            # round trip + the last impatient query
            p = patience[x]
            if 2 * d <= p:
                t = 2 * d
            elif (2 * d) % p == 0:
                t = 4 * d - p
            else:
                t = 2 * d // p * p + 2 * d

            res = max(res, t)

        res += 1
        return res
