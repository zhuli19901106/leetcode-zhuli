# https://leetcode.com/problems/maximum-alternating-subsequence-sum/
# the DP solution is right, but not good enough

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # this is much simpler
        ve, vo = 0, 0
        for x in nums:
            ve1 = max(ve, vo + x)
            vo1 = max(0, max(vo, ve - x))
            ve, vo = ve1, vo1

        return max(ve, vo)

    def maxAlternatingSumTooSlow(self, nums: List[int]) -> int:
        INF = 10 ** 9 + 7

        a = nums
        n = len(a)
        dp = [[0 for j in range(n)] for i in range(n)]

        res = -INF
        cur = -INF
        for i in range(n):
            cur = max(cur, a[i])
            dp[i][0] = cur
            res = max(res, dp[i][0])

        for i in range(1, n):
            cur = -INF
            for j in range(i, n):
                cur = max(cur, dp[j - 1][i - 1])
                if i % 2 == 0:
                    dp[j][i] = cur + a[j]
                else:
                    dp[j][i] = cur - a[j]
                res = max(res, dp[j][i])

        return res