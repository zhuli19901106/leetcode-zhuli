# https://leetcode.com/problems/build-a-matrix-with-conditions/
# topological sort
from collections import deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_order = self.topological(k, rowConditions)
        if len(row_order) < k:
            return []

        col_order = self.topological(k, colConditions)
        if len(col_order) < k:
            return []

        mr, mc = {}, {}
        res = [[0 for j in range(k)] for i in range(k)]
        for i in range(k):
            mr[row_order[i] + 1] = i
            mc[col_order[i] + 1] = i
        for i in range(1, k + 1):
            res[mr[i]][mc[i]] = i
        return res

    def topological(self, n, edges):
        ind = [0 for i in range(n)]
        g = {}
        for x, y in edges:
            # 1-indexed
            x -= 1
            y -= 1
            if not x in g:
                g[x] = set()
            if not y in g:
                g[y] = set()
            
            # there may be repeated edges
            if not y in g[x]:
                g[x].add(y)
                ind[y] += 1

        q = deque()
        for i in range(n):
            if ind[i] == 0:
                q.appendleft(i)

        res = []
        while len(q) > 0:
            x = q.pop()
            res.append(x)

            if not x in g:
                continue

            for y in g[x]:
                if ind[y] == 0:
                    continue

                ind[y] -= 1
                if ind[y] == 0:
                    q.appendleft(y)
        return res
