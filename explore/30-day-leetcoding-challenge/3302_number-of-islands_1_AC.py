# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3302/
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        offs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        g = grid
        n = len(g)
        m = len(g[0]) if n > 0 else 0
        if n == 0 or m == 0:
            return 0

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        q = deque()
        st = set()

        res = 0
        for i in range(n):
            for j in range(m):
                if g[i][j] == '0' or (i, j) in st:
                    continue
                st.add((i, j))
                q.append((i, j))
                while len(q) > 0:
                    x, y = q.popleft()
                    for off in offs:
                        x1, y1 = x + off[0], y + off[1]
                        if not inbound(x1, y1):
                            continue
                        tp = (x1, y1)
                        if g[x1][y1] == '1' and not tp in st:
                            st.add(tp)
                            q.append(tp)
                res += 1
        return res
