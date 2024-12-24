# medium
# https://leetcode.com/problems/maximum-matrix-sum/
# sort of tricky, but acceptable
# if odd number of negatives, leave the one with smallest abs()
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        g = matrix
        n, m = len(g), len(g[0])

        nc = 0
        sm = 0
        min_val = abs(g[0][0])
        for i in range(n):
            for j in range(m):
                if g[i][j] < 0:
                    g[i][j] = -g[i][j]
                    nc += 1
                min_val = min(min_val, abs(g[i][j]))
                sm += g[i][j]

        return sm if nc % 2 == 0 else sm - 2 * min_val
