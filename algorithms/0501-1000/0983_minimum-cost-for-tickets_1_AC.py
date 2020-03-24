# https://leetcode.com/problems/minimum-cost-for-tickets/
# DP solution, took me some 20+ minutes to think it through
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        m = len(costs)
        arr_day = [1, 7, 30]
        idx_day = [0, 0, 0]
        n = len(days)
        INT_MAX = 2 ** 31 - 1
        dp = [INT_MAX for i in range(n + 1)]
        dp[0] = 0
        for i in range(n):
            for j in range(m):
                while idx_day[j] < i and days[i] - days[idx_day[j]] >= arr_day[j]:
                    idx_day[j] += 1
                dp[i + 1] = min(dp[i + 1], dp[idx_day[j]] + costs[j])
        return dp[n]
