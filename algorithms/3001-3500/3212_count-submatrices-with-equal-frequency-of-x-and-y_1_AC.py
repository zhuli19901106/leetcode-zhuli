# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/
# prefix matrix sum
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        g = grid
        n, m = len(g), len(g[0])

        sx = [[0 for j in range(m + 1)] for i in range(n + 1)]
        sy = [[0 for j in range(m + 1)] for i in range(n + 1)]

        for i in range(n):
            for j in range(m):
                x = 1 if g[i][j] == 'X' else 0
                y = 1 if g[i][j] == 'Y' else 0
                sx[i + 1][j + 1] = sx[i + 1][j] + sx[i][j + 1] + x - sx[i][j]
                sy[i + 1][j + 1] = sy[i + 1][j] + sy[i][j + 1] + y - sy[i][j]

        res = 0
        for i in range(n):
            for j in range(m):
                x = sx[i + 1][j + 1]
                y = sy[i + 1][j + 1]
                if x == y and x > 0:
                    res += 1
        return res
