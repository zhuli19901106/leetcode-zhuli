# medium
# https://leetcode.com/problems/number-of-corner-rectangles/
# 1AC, O(n^2) for enumerate, O(n) for set intersection, thus O(n^3)
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        g = grid
        n = len(g)
        m = len(g[0])
        ast = [set() for i in range(n)]
        for i in range(n):
            for j in range(m):
                if g[i][j] == 1:
                    ast[i].add(j)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                st = ast[i] & ast[j]
                k = len(st)
                res += k * (k - 1) // 2
        return res
