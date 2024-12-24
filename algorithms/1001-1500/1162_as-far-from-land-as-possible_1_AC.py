# medium
# https://leetcode.com/problems/as-far-from-land-as-possible/
# 1AC, BFS
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        offs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

        a = grid
        n = len(a)
        m = len(a[0])

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        def border(x, y):
            if not inbound(x, y) or a[x][y] != 1: 
                return False
            cnt = 0
            for off in offs:
                x1, y1 = x + off[0], y + off[1]
                if inbound(x1, y1) and a[x1][y1] == 0:
                    cnt += 1
            return cnt > 0

        q = deque()
        for i in range(n):
            for j in range(m):
                if not border(i, j):
                    continue
                q.append((i, j, 0))
        while len(q) > 0:
            x, y, d = q.popleft()
            for off in offs:
                x1, y1 = x + off[0], y + off[1]
                if inbound(x1, y1) and a[x1][y1] == 0:
                    a[x1][y1] = -(d + 1)
                    q.append((x1, y1, d + 1))
        res = -1
        for i in range(n):
            for j in range(m):
                if a[i][j] < 0 and -a[i][j] > res:
                    res = -a[i][j]
        return res
