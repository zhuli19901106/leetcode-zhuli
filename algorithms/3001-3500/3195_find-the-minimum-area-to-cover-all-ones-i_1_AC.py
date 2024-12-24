# medium
# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        g = grid
        n, m = len(g), len(g[0])
        sm_row = [0 for i in range(n)]
        sm_col = [0 for j in range(m)]
        for i in range(n):
            for j in range(m):
                sm_row[i] += g[i][j]
                sm_col[j] += g[i][j]

        i1, i2 = 0, n - 1
        while i1 <= i2 and (sm_row[i1] == 0 or sm_row[i2] == 0):
            if sm_row[i1] == 0:
                i1 += 1
            if sm_row[i2] == 0:
                i2 -= 1

        j1, j2 = 0, m - 1
        while j1 <= j2 and (sm_col[j1] == 0 or sm_col[j2] == 0):
            if sm_col[j1] == 0:
                j1 += 1
            if sm_col[j2] == 0:
                j2 -= 1

        return (i2 - i1 + 1) * (j2 - j1 + 1)
