# easy
# https://leetcode.com/problems/find-champion-i/
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for j in range(n):
            cc = 0
            for i in range(n):
                cc += grid[i][j]
            if cc == 0:
                return j
        return -1
