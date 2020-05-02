# https://leetcode.com/problems/bus-routes/
# 1AC
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # stops
        ms = defaultdict(set)
        # routes
        sr = set()

        for i, r in enumerate(routes):
            for x in r:
                ms[x].add(i)
        
        mm = {}
        q = deque()
        rst = set()

        mm[S] = 0
        q.append(S)
        while len(q) > 0 and not T in mm:
            x = q.popleft()
            d = mm[x]
            for r in ms[x]:
                # route alreay visited
                if r in rst:
                    continue
                rst.add(r)
                for y in routes[r]:
                    if y in mm:
                        continue
                    mm[y] = d + 1
                    q.append(y)
        return mm[T] if T in mm else -1
