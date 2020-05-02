# https://leetcode.com/problems/cherry-pickup/
# https://leetcode.com/problems/cherry-pickup/discuss/592725/Clean-python-top-down
# I got a similar solution alone, but my code was more clunky compared to this one
from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        g = grid
        n = len(g)
        m = len(g[0])

        # well, actually the LRU cache size was the key to performance
        @lru_cache(None)
        def dfs(ix, iy, jx, jy):
            if ix >= n or iy >= m or jx >= n or jy >= m:
                return -1
            if g[ix][iy] == -1 or g[jx][jy] == -1:
                return -1
            
            if ix == n - 1 and iy == m - 1:
                return g[ix][iy]

            if ix == jx and iy == jy:
                cur = g[ix][iy]
            else:
                cur = g[ix][iy] + g[jx][jy]

            res = -1
            if ix == jx and iy == jy:
                cur = g[ix][iy]
            else:
                cur = g[ix][iy] + g[jx][jy]

            res = max(res, dfs(ix + 1, iy, jx + 1, jy))
            res = max(res, dfs(ix + 1, iy, jx, jy + 1))
            res = max(res, dfs(ix, iy + 1, jx + 1, jy))
            res = max(res, dfs(ix, iy + 1, jx, jy + 1))
            if res == -1:
                return -1
            return res + cur

        res = dfs(0, 0, 0, 0)
        return res if res != -1 else 0
