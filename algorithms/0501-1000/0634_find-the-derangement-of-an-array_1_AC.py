# medium
# https://leetcode.com/problems/find-the-derangement-of-an-array/
# the dp[n - 2] part is bit finicky
class Solution:
    MOD = 10 ** 9 + 7

    def __init__(self):
        self.dp = [0, 0, 1]

    def findDerangement(self, n: int) -> int:
        dp = self.dp
        m = len(dp) - 1
        while m < n:
            dp.append((dp[m - 1] + dp[m]) * m % Solution.MOD)
            m += 1
        return dp[n]
