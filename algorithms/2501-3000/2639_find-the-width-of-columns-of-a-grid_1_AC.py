# easy
# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/
from math import floor, log10

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = [0 for j in range(n)]
        for j in range(n):
            for i in range(m):
                w = self.getWidth(grid[i][j])
                if w > res[j]:
                    res[j] = w
        return res

    def getWidth(self, x):
        if x < 0:
            return self.getWidth(-x) + 1
        if x == 0:
            return 1
        return int(floor(log10(x))) + 1
