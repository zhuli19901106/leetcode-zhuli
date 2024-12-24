# medium
# https://leetcode.com/problems/tree-diameter/
# 1AC, search for the furthest node, then search from that node for the furthest
from collections import deque

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        g = {}
        for x, y in edges:
            if not x in g:
                g[x] = set()
            g[x].add(y)
            if not y in g:
                g[y] = set()
            g[y].add(x)

        def bfs(start_i):
            max_i, max_d = -1, -1

            q = deque()
            st = set()

            st.add(start_i)
            q.append((start_i, 0))
            while len(q) > 0:
                i, d = q.popleft()
                if d > max_d:
                    max_i, max_d = i, d
                for x in g[i]:
                    if x in st:
                        continue
                    st.add(x)
                    q.append((x, d + 1))
            return max_i, max_d

        max_i, max_d = bfs(0)
        max_i, max_d = bfs(max_i)
        return max_d
