# hard
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# Hamilton path, no, don't do it
# when I wasted so much time thinking about it
# it's actually DP + bit manipulations, ridiculous
# my version with Floyd-Warshall won't work
from collections import deque

INT_MAX = (1 << 31) - 1

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n < 2:
            return 0

        res = [INT_MAX for i in range(1 << n)]
        q = deque()
        st = set()

        for i in range(n):
            q.appendleft((i, 1 << i))

        bme = (1 << n) - 1
        d = 0
        while len(q) > 0:
            q1 = deque()
            while len(q) > 0:
                x, bmx = q.pop()
                if (x, bmx) in st:
                    continue
                st.add((x, bmx))

                if bmx == bme:
                    return d
                for y in graph[x]:
                    bmy = bmx | (1 << y)
                    q1.appendleft((y, bmy))
            d += 1
            q = q1

        return -1
