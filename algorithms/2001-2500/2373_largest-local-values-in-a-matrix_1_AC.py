# easy
# https://leetcode.com/problems/largest-local-values-in-a-matrix/
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        res = []
        for i in range(1, n - 1):
            res.append([])
            for j in range(1, m - 1):
                cur = grid[i][j]
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        if grid[i + ii][j + jj] > cur:
                            cur = grid[i + ii][j + jj]
                res[-1].append(cur)

        return res
