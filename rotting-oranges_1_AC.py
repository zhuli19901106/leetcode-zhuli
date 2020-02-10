# https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        offsets = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

        def inbound(i, j):
            return i >= 0 and i <= n - 1 and j >= 0 and j <= m - 1

        def transform(g1, offsets):
            g2 = [[g1[i][j] for j in range(m)] for i in range(n)]
            cnt_rot = 0
            cnt_fresh = 0
            for i in range(n):
                for j in range(m):
                    if g1[i][j] != 1:
                        continue
                    for off in offsets:
                        i1 = i + off[0]
                        j1 = j + off[1]
                        if not inbound(i1, j1) or g1[i1][j1] != 2:
                            continue
                        g2[i][j] = 2
                        cnt_rot += 1
                        break
                    if g1[i][j] == 1:
                        cnt_fresh += 1
            return cnt_fresh, cnt_rot, g2

        g1 = grid
        res = 0
        while True:
            cnt_fresh, cnt_rot, g2 = transform(g1, offsets)
            g1 = g2
            if cnt_rot == 0:
                break
            res += 1
        return res if cnt_fresh == 0 else -1
