# https://leetcode.com/problems/increment-submatrices-by-one/
# from prefix sums to element values
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        sm = [[0 for j in range(n + 1)] for i in range(n + 1)]
        for x1, y1, x2, y2 in queries:
            x2 += 1
            y2 += 1
            if x1 == 0 and y1 == 0:
                sm[x2][y2] += 1
            elif x1 == 0:
                sm[x2][y2] += 1
                sm[x2][y1] -= 1
            elif y1 == 0:
                sm[x2][y2] += 1
                sm[x1][y2] -= 1
            else:
                sm[x2][y2] += 1
                sm[x1][y1] += 1
                sm[x1][y2] -= 1
                sm[x2][y1] -= 1

        for i in range(n, 0, -1):
            # this is tricky
            for j in range(n, 0, -1):
                sm[i - 1][j] += sm[i][j]
            for j in range(n, 0, -1):
                sm[i][j - 1] += sm[i][j]

        mat = [[sm[i + 1][j + 1] for j in range(n)] for i in range(n)]
        return mat
