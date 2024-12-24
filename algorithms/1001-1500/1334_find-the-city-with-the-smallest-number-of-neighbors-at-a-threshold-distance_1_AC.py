# medium
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
# 1AC, Floyd
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INT_MAX = 2 ** 31 - 1
        g = [[INT_MAX for j in range(n)] for i in range(n)]
        for x, y, w in edges:
            g[x][y] = g[y][x] = w

        dt = distanceThreshold
        for k in range(n):
            for i in range(n):
                if g[i][k] == INT_MAX:
                    continue
                for j in range(n):
                    if g[k][j] == INT_MAX:
                        continue
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])

        min_nc = n
        ri = -1
        for i in range(n):
            nc = 0
            for j in range(n):
                if j == i or g[i][j] > dt:
                    continue
                nc += 1
            if nc <= min_nc:
                min_nc = nc
                ri = i
        return ri
