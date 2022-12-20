# https://leetcode.com/problems/unique-paths-iii/
# totally brute-force

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        MAXN = 20
        s = ''.join([chr(ord('a') + i) for i in range(MAXN)])
        offs = [(-1, 0), (+1, 0), (0, -1), (0, + 1)]

        g = grid
        n, m = len(g), len(g[0])
        tot = 2
        sx, sy = -1, -1
        for i in range(n):
            for j in range(m):
                if g[i][j] == 0:
                    tot += 1
                elif g[i][j] == 1:
                    sx, sy = i, j

        def dfs(x, y, path, st, res):
            if g[x][y] == 2:
                if len(st) == tot:
                    res.add(path)
                return

            for off in offs:
                x1, y1 = x + off[0], y + off[1]
                val1 = x1 * m + y1

                if x1 < 0 or x1 > n - 1 or y1 < 0 or y1 > m - 1:
                    continue
                if val1 in st or g[x1][y1] == -1:
                    continue

                st.add(val1)
                dfs(x1, y1, path + s[val1], st, res)
                st.remove(val1)

        st = set()
        res = set()
        sval = sx * m + sy

        st.add(sval)
        dfs(sx, sy, s[sval], st, res)
        st.remove(sval)

        return len(res)
