# https://leetcode.com/problems/path-with-maximum-gold/
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        offs = [(0, +1), (0, -1), (+1, 0), (-1, 0)]
        a = grid
        n = len(a)
        m = len(a[0])
        vs = [[False for j in range(m)] for i in range(n)]

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 <= y <= m - 1

        max_sum = 0
        def traverse(x, y, cur_sum):
            nonlocal a, vs
            nonlocal max_sum
            
            if cur_sum > max_sum:
                max_sum = cur_sum
            for off in offs:
                x1, y1 = x + off[0], y + off[1]
                if not (inbound(x1, y1) and a[x1][y1] > 0 and not vs[x1][y1]):
                    continue
                vs[x1][y1] = True
                traverse(x1, y1, cur_sum + a[x1][y1])
                vs[x1][y1] = False

        for i in range(n):
            for j in range(m):
                if a[i][j] <= 0:
                    continue
                vs[i][j] = True
                traverse(i, j, a[i][j])
                vs[i][j] = False
        return max_sum
