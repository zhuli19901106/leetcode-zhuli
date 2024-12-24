# medium
# https://leetcode.com/problems/shortest-path-in-binary-matrix/
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        offs = [(x // 3 - 1, x % 3 - 1) for x in range(9) if x != 4]
        q = deque()
        st = set()

        g = grid
        n = len(g)

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= n - 1

        sx, sy = 0, 0
        ex, ey = n - 1, n - 1
        if g[sx][sy] == 1 or g[ex][ey] == 1:
            return -1

        st.add((sx, sy))
        q.append((sx, sy, 1))
        while len(q) > 0:
            x, y, d = q.popleft()
            if x == ex and y == ey:
                return d
            for off in offs:
                x1, y1 = x + off[0], y + off[1]
                if not inbound(x1, y1) or g[x1][y1] != 0 or (x1, y1) in st:
                    continue
                st.add((x1, y1))
                q.append((x1, y1, d + 1))
        return -1
