# https://leetcode.com/problems/count-ways-to-build-good-strings/
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # 1e9 is float by default
        MOD = int(1e9 + 7)

        dp = [0 for i in range(high + 1)]
        dp[0] = 1
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            dp[i] %= MOD

        res = 0
        for i in range(low, high + 1):
            res = (res + dp[i]) % MOD
        return res
