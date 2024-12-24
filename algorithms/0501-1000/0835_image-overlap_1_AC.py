# medium
# https://leetcode.com/problems/image-overlap/
# brute-force
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        m = len(A[0])

        def overlap(a, b, ox, oy):
            res = 0
            x1 = max(0, ox)
            y1 = max(0, oy)
            x2 = min(n, n + ox)
            y2 = min(m, m + oy)
            for i in range(x1, x2):
                for j in range(y1, y2):
                    if a[i][j] == 1 and b[i - ox][j - oy] == 1:
                        res += 1
            return res

        res = 0
        for ox in range(-(n - 1), (n - 1) + 1):
            for oy in range(-(m - 1), (m - 1) + 1):
                res = max(res, overlap(A, B, ox, oy))
        return res
