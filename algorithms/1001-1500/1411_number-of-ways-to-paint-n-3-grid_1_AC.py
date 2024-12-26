# hard
# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
# DP
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = int(1e9 + 7)

        dp = [[0 for j in range(27)] for i in range(n)]
        conflict_val = set()
        for x in range(27):
            x1, x2, x3 = self.getDigits(x)
            if x1 != x2 and x2 != x3:
                dp[0][x] = 1
            else:
                conflict_val.add(x)

        conflict_pair = [[False for j in range(27)] for i in range(27)]
        for x in range(27):
            for y in range(x, 27):
                if not self.checkConflict(x, y):
                    continue
                conflict_pair[x][y] = True
                conflict_pair[y][x] = True

        for i in range(1, n):
            for x in range(27):
                if x in conflict_val:
                    continue
                for y in range(27):
                    if conflict_pair[x][y]:
                        continue
                    dp[i][x] = (dp[i][x] + dp[i - 1][y]) % MOD

        res = sum(dp[n - 1]) % MOD
        return res

    def getDigits(self, x):
        return x // 9 % 3, x // 3 % 3, x % 3

    def checkConflict(self, x, y):
        x1, x2, x3 = self.getDigits(x)
        y1, y2, y3 = self.getDigits(y)

        return x1 == y1 or x2 == y2 or x3 == y3
