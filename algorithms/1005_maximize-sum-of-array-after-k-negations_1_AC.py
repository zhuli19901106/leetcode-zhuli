# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        a = sorted(A)
        n = len(a)
        for i in range(n):
            if K > 0 and a[i] < 0:
                a[i] = -a[i]
                K -= 1
        res = sum(a)
        if K > 0 and K % 2 == 1:
            res -= 2 * min(a)
        return res
