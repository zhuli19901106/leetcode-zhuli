# https://leetcode.com/problems/largest-sum-of-averages/
# 1AC, very DP
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        a = A
        n = len(a)
        ps = [0]
        for x in a:
            ps.append(ps[-1] + x)

        dp = [[0 for j in range(n)] for i in range(K)]
        for i in range(n):
            dp[0][i] = ps[i + 1] / (i + 1)
        for ki in range(1, K):
            for i in range(ki, n):
                for j in range(ki - 1, i):
                    dp[ki][i] = max(dp[ki][i], dp[ki - 1][j] +\
                        (ps[i + 1] - ps[j + 1]) / (i - j))
        return dp[K - 1][n - 1]
