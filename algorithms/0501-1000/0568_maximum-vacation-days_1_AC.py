# hard
# https://leetcode.com/problems/maximum-vacation-days/
# standard DP solution
from collections import defaultdict

class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        af = flights
        ad = days
        n = len(ad)
        k = len(ad[0])

        dp = [{}, {}]
        dp[0][0] = ad[0][0]
        for i in range(n):
            if af[0][i] == 1:
                dp[0][i] = ad[i][0]

        f = 1
        nf = 1 - f
        for ki in range(1, k):
            dp[f] = {}
            m1, m2 = dp[nf], dp[f]

            for x, d in m1.items():
                m2[x] = d + ad[x][ki]
            for x, d in m1.items():
                for i in range(n):
                    if af[x][i] == 0:
                        continue
                    cur = d + ad[i][ki]
                    m2[i] = max(m2[i], cur) if i in m2 else cur

            f = 1 - f
            nf = 1 - f
        return max(dp[nf].values())
