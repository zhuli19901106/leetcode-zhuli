# medium
# https://leetcode.com/problems/count-sorted-vowel-strings/
# 1AC, traditional DP
class Solution:
    def countVowelStrings(self, n: int) -> int:
        N = 50
        D = 5
        dp = [[0 for j in range(D)] for i in range(N)]

        for i in range(D):
            dp[0][i] = 1
        for i in range(1, N):
            for j in range(D):
                for k in range(j, D):
                    dp[i][j] += dp[i - 1][k]
        return sum(dp[n - 1])
