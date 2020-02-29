# https://leetcode.com/problems/stone-game/
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        a = piles
        n = len(a)
        ps = [0 for i in range(n + 1)]
        for i in range(n):
            ps[i + 1] = ps[i] + a[i]

        dp = [dict() for i in range(n)]
        for i in range(n):
            dp[i][i] = a[i]
        for i in range(1, n):
            for j in range(0, n - i):
                dp[j][j + i] = max(a[j] + ps[j + i + 1] - ps[j + 1] - dp[j + 1][j + i],\
                    a[j + i] + ps[j + i] - ps[j] - dp[j][j + i - 1])
        return dp[0][n - 1] > ps[n] - ps[0] - dp[0][n - 1]
