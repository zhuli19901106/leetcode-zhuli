# medium
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/
# requires a bit thinking

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        a = matrix
        n, m = len(a), len(a[0])

        for j in range(m):
            cur = 0
            for i in range(n):
                if a[i][j] == 1:
                    a[i][j] += cur
                else:
                    a[i][j] = 0
                cur = a[i][j]

        res = 0
        for i in range(n):
            a[i].sort()
            for j in range(m):
                res = max(res, (m - j) * a[i][j])

        return res
