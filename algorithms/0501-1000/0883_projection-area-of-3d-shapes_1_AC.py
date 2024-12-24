# easy
# https://leetcode.com/problems/projection-area-of-3d-shapes/
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        a = grid
        n = len(a)
        xy = 0
        xz = [0] * n
        yz = [0] * n
        for i in range(n):
            for j in range(n):
                if a[i][j] > 0:
                    xy += 1
                xz[i] = max(xz[i], a[i][j])
                yz[j] = max(yz[j], a[i][j])
        xz = sum(xz)
        yz = sum(yz)
        return xy + xz + yz
