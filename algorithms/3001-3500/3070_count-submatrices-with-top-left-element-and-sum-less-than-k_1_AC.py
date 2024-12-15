# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/
# prefix sum
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        g = grid
        n, m = len(g), len(g[0])
        sm = [[0 for j in range(m + 1)] for i in range(n + 1)]

        res = 0
        for i in range(n) :
            for j in range(m):
                sm[i + 1][j + 1] = sm[i + 1][j] + sm[i][j + 1] + g[i][j] - sm[i][j]
                if sm[i + 1][j + 1] <= k:
                    res += 1
        return res
