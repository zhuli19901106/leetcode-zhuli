# medium
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
# good
from collections import deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ind = [0 for i in range(n)]
        g = {}
        for x, y in edges:
            ind[y] += 1
            if not x in g:
                g[x] = set()
            g[x].add(y)

        res = [set() for i in range(n)]
        q = deque()
        vst = set()
        for x in range(n):
            if ind[x] == 0:
                vst.add(x)
                q.appendleft(x)

        while len(q) > 0:
            x = q.pop()
            if not x in g:
                continue

            for y in g[x]:
                ind[y] -= 1
                res[y] |= {x}

                if y in vst:
                    continue

                res[y] |= res[x]
                if ind[y] == 0:
                    vst.add(y)
                    q.appendleft(y)

        res = [sorted(list(ys)) for ys in res]
        return res
