# medium
# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
# 1AC, binary search with brute force
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        a = mat
        n = len(a)
        m = len(a[0])
        min_val = min([min(r) for r in a])
        if threshold < min_val:
            return 0
        ps = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(n):
            for j in range(m):
                ps[i + 1][j + 1] = a[i][j] + ps[i + 1][j] + ps[i][j + 1] - ps[i][j]

        def sumRect(x1, y1, x2, y2):
            return ps[x2 + 1][y2 + 1] + ps[x1][y1] - ps[x2 + 1][y1] - ps[x1][y2 + 1]

        def check(side, threshold):
            min_val = threshold + 1
            for i in range(n - side + 1):
                for j in range(m - side + 1):
                    sum_val = sumRect(i, j, i + side - 1, j + side - 1)
                    min_val = min(min_val, sum_val)
            return min_val <= threshold

        low = 1
        high = min(n, m)
        if check(high, threshold):
            return high
        while high - low > 1:
            mid = low + (high - low) // 2
            if check(mid, threshold):
                low = mid
            else:
                high = mid
        return low
