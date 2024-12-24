# medium
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        a = matrix
        n = len(a)
        m = len(a[0])
        sa = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(n):
            for j in range(m):
                sa[i + 1][j + 1] = sa[i + 1][j] + sa[i][j + 1] - sa[i][j] + a[i][j]

        def sumRange(x1, y1, x2, y2):
            return sa[x2 + 1][y2 + 1] + sa[x1][y1] - sa[x1][y2 + 1] - sa[x2 + 1][y1]

        res = 0
        for i in range(n):
            for j in range(m):
                k = 1
                while i + k <= n and j + k <= m and\
                    sumRange(i, j, i + k - 1, j + k - 1) == k * k:
                    k += 1
                res += k - 1
        return res
