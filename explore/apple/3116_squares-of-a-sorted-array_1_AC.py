# https://leetcode.com/problems/squares-of-a-sorted-array/
from bisect import bisect_left

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i2 = bisect_left(A, 0)
        i1 = i2 - 1
        res = []
        n = len(A)
        while i1 >= 0 and i2 <= n - 1:
            v1 = A[i1] * A[i1]
            v2 = A[i2] * A[i2]
            if v1 < v2:
                res.append(v1)
                i1 -= 1
            else:
                res.append(v2)
                i2 += 1
        while i1 >= 0:
            v1 = A[i1] * A[i1]
            res.append(v1)
            i1 -= 1
        while i2 <= n - 1:
            v2 = A[i2] * A[i2]
            res.append(v2)
            i2 += 1
        return res
