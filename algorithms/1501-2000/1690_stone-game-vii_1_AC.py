# https://leetcode.com/problems/stone-game-vii/
# DP

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)

        dp = [[0 for j in range(n)] for i in range(n)]
        sm = [0]

        for i in range(n):
            sm.append(stones[i] + sm[-1])

        for i in range(1, n):
            for j in range(0, n - i):
                k = j + i
                dp[j][k] = max((sm[k + 1] - sm[j + 1]) - dp[j + 1][k], \
                    (sm[k] - sm[j]) - dp[j][k - 1])

        return dp[0][n - 1]
