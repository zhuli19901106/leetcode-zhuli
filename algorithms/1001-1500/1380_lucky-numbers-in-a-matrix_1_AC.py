# easy
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/
# 1AC
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -(2 ** 31)
        a = matrix
        n = len(a)
        m = len(a[0])
        min_row = [INT_MAX for i in range(n)]
        max_col = [INT_MIN for i in range(m)]
        for i in range(n):
            for j in range(m):
                min_row[i] = min(min_row[i], a[i][j])
                max_col[j] = max(max_col[j], a[i][j])

        res = []
        for i in range(n):
            for j in range(m):
                if a[i][j] == min_row[i] and a[i][j] == max_col[j]:
                    res.append(a[i][j])
        return res
