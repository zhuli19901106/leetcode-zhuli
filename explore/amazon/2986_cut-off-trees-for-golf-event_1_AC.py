# https://leetcode.com/problems/cut-off-trees-for-golf-event/
# simple idea, but basically brute-force
from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        f = forest
        n = len(f)
        m = len(f[0])
        offs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        def bfs(sx, sy, ex, ey):
            q = deque()
            mm = {}

            mm[(sx, sy)] = 0
            q.append((sx, sy))
            while len(q) > 0 and not (ex, ey) in mm:
                x, y = q.popleft()
                d = mm[(x, y)]
                for off in offs:
                    x1, y1 = x + off[0], y + off[1]
                    if not inbound(x1, y1) or f[x1][y1] == 0 or (x1, y1) in mm:
                        continue
                    mm[(x1, y1)] = d + 1
                    q.append((x1, y1))
            return mm[(ex, ey)] if (ex, ey) in mm else -1

        path = []
        for x in range(n):
            for y in range(m):
                if f[x][y] > 1:
                    path.append((f[x][y], x, y))
        path.sort()
        sx, sy = 0, 0
        res = 0
        for _, x, y in path:
            ex, ey = x, y
            d = bfs(sx, sy, ex, ey)
            if d == -1:
                return -1
            res += d
            sx, sy = ex, ey
        return res
