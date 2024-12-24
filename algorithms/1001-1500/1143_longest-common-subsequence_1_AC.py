# medium
# https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0 for j in range(n2 + 1)] for i in range(2)]
        f = 0
        nf = 1 - f
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[f][j] = dp[nf][j - 1] + 1
                else:
                    dp[f][j] = max(dp[f][j - 1], dp[nf][j])
            f = 1 - f
            nf = 1 - f
        return dp[nf][n2]
