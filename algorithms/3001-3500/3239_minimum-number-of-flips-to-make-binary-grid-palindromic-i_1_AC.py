# medium
# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        g = grid
        n, m = len(g), len(g[0])

        # flip rows
        res_row = 0
        for i in range(n):
            j1, j2 = 0, m - 1
            while j1 < j2:
                if g[i][j1] != g[i][j2]:
                    res_row += 1
                j1 += 1
                j2 -= 1

        # flip columns
        res_col = 0
        for j in range(m):
            i1, i2 = 0, n - 1
            while i1 < i2:
                if g[i1][j] != g[i2][j]:
                    res_col += 1
                i1 += 1
                i2 -= 1

        return min(res_row, res_col)
