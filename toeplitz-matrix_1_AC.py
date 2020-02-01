# https://leetcode.com/problems/toeplitz-matrix/
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        a = matrix
        n = len(a)
        m = len(a[0])
        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        ap0 = [(i, 0) for i in range(n)] + [(0, i) for i in range(1, m)]
        for x0, y0 in ap0:
            x, y = x0, y0
            while inbound(x + 1, y + 1):
                if a[x][y] != a[x + 1][y + 1]:
                    break
                x += 1
                y += 1
            if inbound(x + 1, y + 1):
                return False
        return True
