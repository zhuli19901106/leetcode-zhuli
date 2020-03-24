# https://leetcode.com/problems/partition-array-for-maximum-sum/
# straightforward DP
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        a = A
        n = len(a)

        amax = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            amax[i][i] = a[i]
        for i in range(n):
            for j in range(i + 1, n):
                amax[i][j] = max(amax[i][j - 1], a[j])

        k = K
        dp = [0 for i in range(n + 1)]
        dp[0] = a[0]
        for i in range(1, n):
            dp[i] = 0
            if i < k:
                dp[i] = max(dp[i], amax[0][i] * (i + 1))
            j = 1
            while j <= k and i - j >= 0:
                dp[i] = max(dp[i], dp[i - j] + amax[i - j + 1][i] * j)
                j += 1
        return dp[n - 1]
