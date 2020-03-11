# https://leetcode.com/problems/coin-change-2/
# knapsack
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = amount
        dp = [0 for i in range(n + 1)]

        dp[0] = 1
        for c in coins:
            for i in range(c, n + 1):
                dp[i] += dp[i - c]
        return dp[n]
