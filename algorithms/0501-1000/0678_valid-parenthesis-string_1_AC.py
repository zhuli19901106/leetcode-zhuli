# medium
# https://leetcode.com/problems/valid-parenthesis-string/
# O(n^3) brute-force DP
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True

        dp = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = (s[i] == '*')
        for i in range(n - 1):
            dp[i + 1][i] = True
        for i in range(1, n):
            for j in range(0, n - i):
                j1 = j + i
                val = 0
                if s[j] == '(' or s[j] == '*':
                    val |= 1
                if s[j1] == ')' or s[j1] == '*':
                    val |= 2
                if val == 3 and dp[j + 1][j1 - 1]:
                    dp[j][j1] = True
                    continue

                for k in range(j, j1):
                    if dp[j][k] and dp[k + 1][j1]:
                        dp[j][j1] = True
                        break
        return dp[0][n - 1]
