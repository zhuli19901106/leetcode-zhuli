# medium
# https://leetcode.com/problems/number-of-enclaves/
# 1AC
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        offs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        a = A
        n = len(a)
        m = len(a[0])

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        def flood(x, y, old_val, new_val):
            a[x][y] = new_val
            for off in offs:
                x1, y1 = x + off[0], y + off[1]
                if not (inbound(x1, y1) and a[x1][y1] == old_val):
                    continue
                flood(x1, y1, old_val, new_val)

        for i in range(n):
            for j in (0, m - 1):
                if a[i][j] == 1:
                    flood(i, j, 1, 2)
        for j in range(m):
            for i in (0, n - 1):
                if a[i][j] == 1:
                    flood(i, j, 1, 2)
        res = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == 1:
                    res += 1
        return res
