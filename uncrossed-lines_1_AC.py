# https://leetcode.com/problems/uncrossed-lines/
# exactly LCS problem
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n1 = len(A)
        n2 = len(B)
        dp = [[0 for j in range(n2 + 1)] for i in range(2)]
        f = 0
        nf = 1 - f
        for i in range(n1):
            for j in range(n2):
                if A[i] == B[j]:
                    dp[f][j + 1] = dp[nf][j] + 1
                else:
                    dp[f][j + 1] = max(dp[f][j], dp[nf][j + 1])
            f = 1 - f
            nf = 1 - f
        return dp[nf][n2]
