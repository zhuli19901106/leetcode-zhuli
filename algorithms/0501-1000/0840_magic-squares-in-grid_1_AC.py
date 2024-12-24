# medium
# https://leetcode.com/problems/magic-squares-in-grid/
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(g, x, y, n):
            st = set()
            sr = [0 for i in range(n)]
            sc = [0 for i in range(n)]
            sd = 0
            sad = 0
            for i in range(n):
                for j in range(n):
                    val = g[x + i][y + j]
                    st.add(val)
                    sr[i] += val
                    sc[j] += val
                    if i == j:
                        sd += val
                    if i + j == n - 1:
                        sad += val
            for i in range(n):
                if not i + 1 in st:
                    return False
            s = (1 + n * n) * n // 2
            for i in range(n):
                if sr[i] != s or sc[i] != s:
                    return False
            if sd != s or sad != s:
                return False
            return True

        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n - 3 + 1):
            for j in range(m - 3 + 1):
                if check(grid, i, j, 3):
                    res += 1
        return res
