# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# better O(n + m) solution
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        a = grid
        n, m = len(a), len(a[0])
        x, y = n - 1, 0
        while y <= m - 1 and a[x][y] >= 0:
            y += 1

        res = 0
        while y <= m - 1:
            res += m - y
            x -= 1
            if x < 0:
                break
            while y <= m - 1 and a[x][y] >= 0:
                y += 1
        return res
