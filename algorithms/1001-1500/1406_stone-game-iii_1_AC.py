# hard
# https://leetcode.com/problems/stone-game-iii/
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        INT_MAX = (1 << 31) - 1

        sv = stoneValue
        n = len(sv)

        # this records the best diff of Alice - Bob
        dp = [-INT_MAX for i in range(n + 1)]
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            sm = 0
            for j in range(i, min(i + 3, n)):
                sm += sv[j]
                dp[i] = max(dp[i], sm - dp[j + 1])

        return 'Alice' if dp[0] > 0 else ('Bob' if dp[0] < 0 else 'Tie')
