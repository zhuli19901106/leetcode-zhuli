# medium
# https://leetcode.com/problems/minimum-cost-to-convert-string-i/
# a tiny Floyd, you see the graph, right?
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        MAXC = 26
        g = [[-1 for j in range(MAXC)] for i in range(MAXC)]
        for i in range(MAXC):
            g[i][i] = 0

        ne = len(original)
        for i in range(ne):
            x = ord(original[i]) - ord('a')
            y = ord(changed[i]) - ord('a')
            if g[x][y] == -1 or g[x][y] > cost[i]:
                g[x][y] = cost[i]

        # Floyd here
        for k in range(MAXC):
            for i in range(MAXC):
                for j in range(MAXC):
                    if g[i][k] == -1 or g[k][j] == -1:
                        continue
                    if g[i][j] == -1 or g[i][j] > g[i][k] + g[k][j]:
                        g[i][j] = g[i][k] + g[k][j]

        res = 0
        n = len(source)
        for i in range(n):
            x = ord(source[i]) - ord('a')
            y = ord(target[i]) - ord('a')
            if g[x][y] == -1:
                return -1
            res += g[x][y]
        return res
