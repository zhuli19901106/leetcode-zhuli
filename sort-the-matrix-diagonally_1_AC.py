# https://leetcode.com/problems/sort-the-matrix-diagonally/
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        def sortDiag(x0, y0):
            a = []
            x, y = x0, y0
            while inbound(x, y):
                a.append(mat[x][y])
                x, y = x + 1, y + 1
            a.sort()
            x, y = x0, y0
            for val in a:
                mat[x][y] = val
                x, y = x + 1, y + 1

        for i in range(n):
            sortDiag(i, 0)
        for i in range(1, m):
            sortDiag(0, i)
        return mat
