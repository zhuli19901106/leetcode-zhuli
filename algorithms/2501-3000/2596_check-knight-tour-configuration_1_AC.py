# https://leetcode.com/problems/check-knight-tour-configuration/
# top left must be 0, yeah, right
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        g = grid
        n = len(g)
        if g[0][0] != 0:
            return False

        offs = [
            (-2, -1), (-2, +1), (+2, -1), (+2, +1),
            (-1, -2), (-1, +2), (+1, -2), (+1, +2),
        ]
        offs = set(offs)

        a = []
        for i in range(n):
            for j in range(n):
                a.append((g[i][j], i, j))
        a.sort()

        n2 = n * n
        for i in range(n2 - 1):
            di, dj = a[i + 1][1] - a[i][1], a[i + 1][2] - a[i][2]
            if not (di, dj) in offs:
                return False
        return True
