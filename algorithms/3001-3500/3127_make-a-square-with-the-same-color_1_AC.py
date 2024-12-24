# easy
# https://leetcode.com/problems/make-a-square-with-the-same-color/
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        g = grid
        n, m = len(g), len(g[0])

        sm = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(n):
            for j in range(m):
                sm[i + 1][j + 1] = sm[i][j + 1] + sm[i + 1][j] + \
                    (1 if g[i][j] == 'B' else 0) - sm[i][j]

        for i in range(1, n):
            for j in range(1, m):
                cc = sm[i + 1][j + 1] + sm[i - 1][j - 1] - sm[i + 1][j - 1] - sm[i - 1][j + 1]
                if cc != 2:
                    return True
        return False
