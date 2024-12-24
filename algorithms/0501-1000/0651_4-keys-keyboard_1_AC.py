# medium
# https://leetcode.com/problems/4-keys-keyboard/
# 1AC, O(n) DP solution, I got the wrong idea on first attempt
class Solution:
    def __init__(self):
        n = 50
        dp = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = max(dp[i], dp[i - 1] + 1)
            mul = 2
            # keep pasting once copied
            for j in range(i - 2):
                dp[i] = max(dp[i], (i - j - 1) * dp[j])
        self.dp = dp

    def maxA(self, N: int) -> int:
        return self.dp[N]
