# easy
# https://leetcode.com/problems/check-if-grid-satisfies-conditions/
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        g = grid
        n, m = len(g), len(g[0])
        for i in range(n):
            for j in range(m):
                if i < n - 1 and g[i][j] != g[i + 1][j]:
                    return False
                if j < m - 1 and g[i][j] == g[i][j + 1]:
                    return False
        return True
