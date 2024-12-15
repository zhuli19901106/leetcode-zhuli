# https://leetcode.com/problems/sum-in-a-matrix/
# an easy medium
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        a = nums
        n, m = len(a), len(a[0])
        for r in a:
            r.sort()

        res = 0
        for j in range(m):
            mx = a[0][j]
            for i in range(1, n):
                mx = max(mx, a[i][j])
            res += mx
        return res
