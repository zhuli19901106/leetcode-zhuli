# hard
# https://leetcode.com/problems/count-fertile-pyramids-in-a-land/
# it's actually easier to simply count it

class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        g = grid
        n, m = len(g), len(g[0])

        pref_sm = [[0 for j in range(m + 1)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                pref_sm[i][j + 1] = pref_sm[i][j] + g[i][j]

        res = 0

        # count for pyramids
        ac1 = [[0 for j in range(m)] for i in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(1, m - 1):
                cur_sm = pref_sm[i + 1][j + 2] - pref_sm[i + 1][j - 1]
                if not (g[i][j] == 1 and cur_sm == 3):
                    continue

                ac1[i][j] = 1

                i1, j1 = i + 1, j - 1
                i2, j2 = i + 1, j + 1
                ac1[i][j] += min(ac1[i1][j1], ac1[i2][j2])

                res += ac1[i][j]

        # count for inverse pyramids
        ac2 = [[0 for j in range(m)] for i in range(n)]
        for i in range(1, n):
            for j in range(1, m - 1):
                cur_sm = pref_sm[i - 1][j + 2] - pref_sm[i - 1][j - 1]
                if not (g[i][j] == 1 and cur_sm == 3):
                    continue

                ac2[i][j] = 1

                i1, j1 = i - 1, j - 1
                i2, j2 = i - 1, j + 1
                ac2[i][j] += min(ac2[i1][j1], ac2[i2][j2])

                res += ac2[i][j]

        return res
