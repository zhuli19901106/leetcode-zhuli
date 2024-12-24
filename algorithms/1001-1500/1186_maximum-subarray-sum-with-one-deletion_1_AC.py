# medium
# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
# 1AC, prefix and postfix max subarray
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        INT_MIN = -(2 ** 31)

        a = arr
        n = len(a)
        sm1 = [0 for i in range(n)]
        sm2 = [0 for i in range(n)]

        sm = 0
        max_sm = INT_MIN
        for i in range(n):
            sm += a[i]
            sm1[i] = sm
            max_sm = max(max_sm, sm)
            sm = max(sm, 0)

        sm = 0
        for i in range(n - 1, -1, -1):
            sm += a[i]
            sm2[i] = sm
            sm = max(sm, 0)

        res = max_sm
        for i in range(n - 2):
            res = max(res, sm1[i] + sm2[i + 2])
        return res
