# https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/
# really tiring and tricky
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        g = grid
        n, m = len(g), len(g[0])

        ans = [[-1 for j in range(m)] for i in range(n)]
        for j in range(m):
            self.traverse(g, 0, j, ans)
        for i in range(1, n):
            self.traverse(g, i, 0, ans)
        return ans

    def traverse(self, grid, i0, j0, ans):
        g = grid
        n, m = len(g), len(g[0])

        m1, m2 = {}, {}
        i, j = i0 + 1, j0 + 1
        while i < n and j < m:
            x = g[i][j]
            if not x in m2:
                m2[x] = 1
            else:
                m2[x] += 1
            i += 1
            j += 1

        i, j = i0 + 1, j0 + 1
        while i < n and j < m:
            ans[i - 1][j - 1] = abs(len(m1) - len(m2))

            x, y = g[i - 1][j - 1], g[i][j]
            if not x in m1:
                m1[x] = 1
            else:
                m1[x] += 1
            m2[y] -= 1
            if m2[y] == 0:
                del m2[y]

            i += 1
            j += 1
        ans[i - 1][j - 1] = abs(len(m1) - len(m2))
