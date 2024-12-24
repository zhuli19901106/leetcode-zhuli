# medium
# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/
# 1AC, simple idea, but too much work for an interview question
from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # down, up, right, left
        offs = [(+1, 0), (-1, 0), (0, +1), (0, -1)]
        adjs = {\
            1: [{}, {}, {1, 3, 5}, {1, 4, 6}],\
            2: [{2, 5, 6}, {2, 3, 4}, {}, {}],\
            3: [{2, 5, 6}, {}, {}, {1, 4, 6}],\
            4: [{2, 5, 6}, {}, {1, 3, 5}, {}],\
            5: [{}, {2, 3, 4}, {}, {1, 4, 6}],\
            6: [{}, {2, 3, 4}, {1, 3, 5}, {}],\
        }

        vst = set()
        q = deque()
        g = grid
        n = len(g)
        m = len(g[0])

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        vst.add((0, 0))
        q.append((0, 0))
        while len(q) > 0:
            x, y = q.popleft()
            if x == n - 1 and y == m - 1:
                return True
            v = g[x][y]
            for oi, off in enumerate(offs):
                x1, y1 = x + off[0], y + off[1]
                if not inbound(x1, y1) or (x1, y1) in vst:
                    continue
                # not connected in this direction
                if not g[x1][y1] in adjs[v][oi]:
                    continue
                vst.add((x1, y1))
                q.append((x1, y1))
        return False
