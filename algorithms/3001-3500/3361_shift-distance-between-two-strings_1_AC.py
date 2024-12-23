# https://leetcode.com/problems/shift-distance-between-two-strings/
# make a tiny graph
class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        MAXC = 26
        g = [[-1 for j in range(MAXC)] for i in range(MAXC)]
        for i in range(MAXC):
            g[i][i] = 0

            j = (i + 1) % MAXC
            g[i][j] = nextCost[i]

            j = (i + MAXC - 1) % MAXC
            g[i][j] = previousCost[i]

        for k in range(MAXC):
            for i in range(MAXC):
                for j in range(MAXC):
                    if g[i][k] == -1 or g[k][j] == -1:
                        continue
                    if g[i][j] == -1 or g[i][j] > g[i][k] + g[k][j]:
                        g[i][j] = g[i][k] + g[k][j]

        res = 0
        n = len(s)
        for i in range(n):
            x = ord(s[i]) - ord('a')
            y = ord(t[i]) - ord('a')
            res += g[x][y]
        return res
