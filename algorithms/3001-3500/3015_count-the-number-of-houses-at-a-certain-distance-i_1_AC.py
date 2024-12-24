# medium
# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/
# looks like Floyd, beware of edge cases
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        g = {}
        for i in range(n):
            g[i] = set()
        for i in range(n - 1):
            g[i].add(i + 1)
            g[i + 1].add(i)

        if x != y:
            x -= 1
            y -= 1
            g[x].add(y)
            g[y].add(x)

        dist = [[-1 for j in range(n)] for i in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for x in g:
            for y in g[x]:
                dist[x][y] = 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] == -1 or dist[k][j] == -1:
                        continue
                    if dist[i][j] == -1 or dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        res = [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if dist[i][j] > 0:
                    res[dist[i][j] - 1] += 1
        return res
