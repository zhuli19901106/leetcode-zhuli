# medium
# https://leetcode.com/problems/number-of-distinct-islands/
# 1AC, simple idea but too much work
from collections import deque

class Solution:
    INT_MAX = 2 ** 31 - 1

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        offs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        g = grid
        n = len(g)
        m = len(g[0])

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        def flood(x, y, old_val, new_val):
            q = deque()
            res = []

            g[x][y] = new_val
            q.append((x, y))
            res.append((x, y))
            while len(q) > 0:
                x, y = q.popleft()
                for off in offs:
                    x1, y1 = x + off[0], y + off[1]
                    if inbound(x1, y1) and g[x1][y1] == old_val:
                        g[x1][y1] = new_val
                        q.append((x1, y1))
                        res.append((x1, y1))
            return res

        def encode(ps):
            min_x, min_y = Solution.INT_MAX, Solution.INT_MAX
            for x, y in ps:
                min_x = min(min_x, x)
                min_y = min(min_y, y)
            res = []
            for x, y in ps:
                res.append(chr(x - min_x))
                res.append(chr(y - min_y))
            return ''.join(res)

        st = set()
        for i in range(n):
            for j in range(m):
                if g[i][j] != 1:
                    continue
                ps = flood(i, j, 1, 2)
                st.add(encode(ps))
        return len(st)
