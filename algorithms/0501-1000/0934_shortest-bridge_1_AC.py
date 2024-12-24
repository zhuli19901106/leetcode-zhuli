# medium
# https://leetcode.com/problems/shortest-bridge/
# DFS + BFS, not so smart, but OK
from collections import deque

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        offs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        a = A
        n = len(a)
        m = len(a[0])

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        def flood(x, y, old_val, new_val):
            nonlocal a

            a[x][y] = new_val
            for off in offs:
                x1, y1 = x + off[0], y + off[1]
                if inbound(x1, y1) and a[x1][y1] == old_val:
                    flood(x1, y1, old_val, new_val)

        for i in range(n):
            for j in range(m):
                if a[i][j] == 1:
                    flood(i, j, 1, 2)
                    break
            if a[i][j] == 2:
                break

        q = deque()
        vs = set()
        for i in range(n):
            for j in range(m):
                if a[i][j] == 1:
                    vs.add((i, j))
                    q.append(((i, j, 0)))

        min_d = None
        while len(q) > 0:
            i, j, d = q.popleft()
            for off in offs:
                i1, j1 = i + off[0], j + off[1]
                if not inbound(i1, j1) or (i1, j1) in vs or a[i1][j1] == 1:
                    continue
                if a[i1][j1] == 2:
                    min_d = d
                    break
                if a[i1][j1] == 0:
                    vs.add((i1, j1))
                    q.append((i1, j1, d + 1))
            if not min_d is None:
                break
        return min_d
