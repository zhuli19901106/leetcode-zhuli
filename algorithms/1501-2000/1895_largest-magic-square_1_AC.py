# https://leetcode.com/problems/largest-magic-square/
# just BF
# this is insane
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        g = grid
        n, m = len(g), len(g[0])

        # prefix sums for rows and cols
        rs = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            sm = 0
            for j in range(m):
                sm += g[i][j]
                rs[i][j] = sm
        cs = [[0 for j in range(m)] for i in range(n)]
        for j in range(m):
            sm = 0
            for i in range(n):
                sm += g[i][j]
                cs[i][j] = sm

        ds1 = {}
        ids = []
        ids += zip([0] * m, range(m))
        ids += zip(range(1, n), [0] * (n - 1))
        for si, sj in ids:
            ds1[(si, sj)] = {}
            sm = 0
            i, j = si, sj
            while i < n and j < m:
                sm += g[i][j]
                ds1[(si, sj)][(i, j)] = sm
                i += 1
                j += 1

        ds2 = {}
        ids = []
        ids += zip([0] * m, range(m))
        ids += zip(range(1, n), [m - 1] * (n - 1))
        for si, sj in ids:
            ds2[(si, sj)] = {}
            sm = 0
            i, j = si, sj
            while i < n and j > -1:
                sm += g[i][j]
                ds2[(si, sj)][(i, j)] = sm
                i += 1
                j -= 1

        for r in g:
            print(r)
        print()

        res = 1
        for i in range(n):
            for j in range(m):
                res = max(res, self.checkMagicSquare(i, j, g, rs, cs, ds1, ds2))
        return res

    # check for magic square with top left at (x, y)
    def checkMagicSquare(self, x, y, g, rs, cs, ds1, ds2):
        n, m = len(g), len(g[0])

        res = 1
        d = 1
        while True:
            x1, y1 = d + x, d + y
            if x1 > n - 1 or y1 > m - 1:
                break

            st = set()

            # row sum
            for i in range(x, x1 + 1):
                sm = rs[i][y1] - (rs[i][y - 1] if y > 0 else 0)
                st.add(sm)

            # col sum
            for j in range(y, y1 + 1):
                sm = cs[x1][j] - (cs[x - 1][j] if x > 0 else 0)
                st.add(sm)

            # diagonal sum
            sx, sy = x - min(x, y), y - min(x, y)
            sm1 = ds1[(sx, sy)][(x - 1, y - 1)] if x > 0 and y > 0 else 0
            sm2 = ds1[(sx, sy)][(x1, y1)]
            sm = sm2 - sm1
            st.add(sm)

            # antidiagonal sum (ridiculous)
            sx, sy = (0, y1 + x) if x < m - 1 - y1 else (x - (m - 1 - y1), m - 1)
            sm1 = ds2[(sx, sy)][(x - 1, y1 + 1)] if x > 0 and y1 < m - 1 else 0
            sm2 = ds2[(sx, sy)][(x1, y)]
            sm = sm2 - sm1
            st.add(sm)

            if len(st) == 1:
                res = d + 1

            d += 1

        return res
