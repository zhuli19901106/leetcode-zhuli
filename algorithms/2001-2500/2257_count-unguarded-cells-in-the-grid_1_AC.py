# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
# BFS, a bit slow
from collections import deque

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 0 for free, -1 for wall, 1 for guard, 2 for guarded
        STATE_WALL = -1
        STATE_FREE = 0
        STATE_GUARD = 1
        STATE_GUARDED = 2

        # [0, 1, 2, 3] for [top, bottom, left, right]
        off = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

        g = [[STATE_FREE for j in range(n)] for i in range(m)]
        res = m * n
        q = deque()
        for x, y in guards:
            g[x][y] = STATE_GUARD
            res -= 1
            for i in range(4):
                q.appendleft((x, y, i))

        for x, y in walls:
            g[x][y] = STATE_WALL
            res -= 1

        while len(q) > 0:
            x, y, i = q.pop()
            x1, y1 = x + off[i][0], y + off[i][1]
            if x1 < 0 or x1 > m - 1 or y1 < 0 or y1 > n - 1:
                continue
            if not (g[x1][y1] == STATE_FREE or g[x1][y1] == STATE_GUARDED):
                continue
            if g[x1][y1] == STATE_FREE:
                g[x1][y1] = STATE_GUARDED
                res -= 1
            q.appendleft((x1, y1, i))
        return res
