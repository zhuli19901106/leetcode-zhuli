# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        g = grid
        n = len(g)
        m = len(g[0])
        ar = [0 for i in range(n)]
        ac = [0 for i in range(m)]
        for i in range(n):
            for j in range(m):
                ar[i] = max(ar[i], g[i][j])
                ac[j] = max(ac[j], g[i][j])
        res = 0
        for i in range(n):
            for j in range(m):
                res += min(ar[i], ac[j]) - g[i][j]
        return res
