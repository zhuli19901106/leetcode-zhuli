# https://leetcode.com/problems/where-will-the-ball-fall/
# 1AC, interesting problem, do some simulation
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        res = []
        n = len(grid[0])
        for i in range(n):
            res.append(self.dropBall(grid, i))
        return res

    def dropBall(self, g, y):
        m, n = len(g), len(g[0])
        x = 0
        # 0 for horizontal, 1 for vertical
        dir = 0
        while True:
            if dir == 0:
                if g[x][y] == 1 and y + 1 <= n - 1 and g[x][y + 1] == 1:
                    y += 1
                    dir = 1 - dir
                elif g[x][y] == -1 and y - 1 >= 0 and g[x][y - 1] == -1:
                    y -= 1
                    dir = 1 - dir
                else:
                    break
            else:
                if x == m - 1:
                    break
                x += 1
                dir = 1 - dir
        return y if x == m - 1 and dir == 1 else -1
