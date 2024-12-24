# medium
# https://leetcode.com/problems/matrix-block-sum/
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        sum_mat = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(n):
            for j in range(m):
                sum_mat[i + 1][j + 1] = sum_mat[i + 1][j] + sum_mat[i][j + 1]\
                    + mat[i][j] - sum_mat[i][j]
        res = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                x1 = max(0, i - K)
                y1 = max(0, j - K)
                x2 = min(n - 1, i + K)
                y2 = min(m - 1, j + K)
                res[i][j] = sum_mat[x1][y1] + sum_mat[x2 + 1][y2 + 1]\
                    - sum_mat[x1][y2 + 1] - sum_mat[x2 + 1][y1]
        return res
