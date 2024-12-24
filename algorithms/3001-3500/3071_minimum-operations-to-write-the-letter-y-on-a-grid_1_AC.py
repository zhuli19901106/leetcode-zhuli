# medium
# https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/
# count and calculate
class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        cy, cn = [0, 0, 0], [0, 0, 0]
        n = len(grid)
        m = n // 2
        for i in range(n):
            for j in range(n):
                x = grid[i][j]
                if (i == j and i <= m) or \
                    (i + j == n - 1 and i <= m) or \
                    (j == m and i >= m):
                    cy[x] += 1
                else:
                    cn[x] += 1

        res = n * n
        smy, smn = sum(cy), sum(cn)
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                res = min(res, smy - cy[i] + smn - cn[j])
        return res
