# medium
# https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/
# due to the tiny scale, it doesn't matter how you do it
from math import log

class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        b = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(i, n):
                b[i][j] = self.isBeautiful(s[i: j + 1])

        dp = [[-1 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1 if s[i] == '1' else -1
        for d in range(1, n):
            for i in range(n - d):
                j = i + d
                if b[i][j]:
                    dp[i][j] = 1
                    continue

                for k in range(i, j):
                    if dp[i][k] == -1 or not b[k + 1][j]:
                        continue
                    val = dp[i][k] + 1

                    if dp[i][j] == -1 or dp[i][j] > val:
                        dp[i][j] = val

        return dp[0][n - 1]

    def isBeautiful(self, s):
        if s[0] == '0':
            return False

        x = int(s, 2)
        return 5 ** int(log(x) / log(5)) == x
