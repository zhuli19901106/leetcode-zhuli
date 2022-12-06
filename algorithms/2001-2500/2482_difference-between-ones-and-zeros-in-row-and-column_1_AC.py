# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        g = grid
        n, m = len(g), len(g[0])
        ar = [0 for _ in range(n)]
        ac = [0 for _ in range(m)]

        for i in range(n):
            for j in range(m):
                if g[i][j] == 1:
                    ar[i] += 1
                    ac[j] += 1
        df = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                df[i][j] = 2 * ar[i] + 2 * ac[j] - n - m

        return df
