# https://leetcode.com/problems/modify-the-matrix/
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        mat = matrix

        n, m = len(mat), len(mat[0])
        col_max = [-1 for j in range(m)]

        for i in range(n):
            for j in range(m):
                col_max[j] = max(col_max[j], mat[i][j])

        ans = [[-1 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == -1:
                    ans[i][j] = col_max[j]
                else:
                    ans[i][j] = mat[i][j]
        return ans
