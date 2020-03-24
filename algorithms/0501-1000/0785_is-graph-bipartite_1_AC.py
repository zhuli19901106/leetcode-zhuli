# https://leetcode.com/problems/is-graph-bipartite/
# BFS or DFS, either will do
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        g = graph
        n = len(g)
        res = [-1 for i in range(n)]

        q = deque()
        for i in range(n):
            if res[i] != -1:
                continue
            res[i] = 0
            q.append(i)
            while len(q) > 0:
                j = q.popleft()
                val = res[j]
                for j1 in g[j]:
                    if res[j1] == val:
                        return False
                    if res[j1] == -1:
                        res[j1] = 1 - val
                        q.append(j1)
        return True
