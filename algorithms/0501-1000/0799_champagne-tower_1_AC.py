# medium
# https://leetcode.com/problems/champagne-tower/
# a rather classic hard medium, just simulate and don't try any magic
# it's most likely that you'll find this much harder if you try anything smarter
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        n = query_row + 1
        a = [[0.0 for j in range(i + 1)] for i in range(n)]

        a[0][0] = poured
        for i in range(1, n):
            for j in range(i):
                p = max(a[i - 1][j] - 1.0, 0)
                a[i][j] += 0.5 * p
                a[i][j + 1] += 0.5 * p
                a[i - 1][j] = min(a[i - 1][j], 1.0)
        for j in range(n):
            a[n - 1][j] = min(a[n - 1][j], 1.0)

        return a[query_row][query_glass]
