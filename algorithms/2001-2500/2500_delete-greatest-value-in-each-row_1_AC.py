# https://leetcode.com/problems/delete-greatest-value-in-each-row/
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(n):
            grid[i].sort()
        sm = 0
        for j in range(m):
            max_val = 0
            for i in range(n):
                if grid[i][j] > max_val:
                    max_val = grid[i][j]
            sm += max_val

        return sm
