from collections import defaultdict, deque
from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        INT_MAX = 2 ** 31 - 1

        md = {}
        g = defaultdict(dict)
        for x, y, d in times:
            g[x][y] = d
        for i in range(1, N + 1):
            md[i] = INT_MAX

        pq = []
        st = set()

        md[K] = 0
        heappush(pq, (0, K))
        while len(pq) > 0:
            d, x = heappop(pq)
            st.add(x)
            if d > md[x]:
                continue
            for y in g[x]:
                if y in st:
                    # visited
                    continue
                if md[x] + g[x][y] < md[y]:
                    md[y] = md[x] + g[x][y]
                    heappush(pq, (md[y], y))
        res = 0
        for v in md.values():
            res = max(res, v)
        return res if res < INT_MAX else -1
