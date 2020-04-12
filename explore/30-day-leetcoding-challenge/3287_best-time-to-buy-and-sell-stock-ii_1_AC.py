# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3287/
# 1AC
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = prices
        n = len(p)
        res = 0
        for i in range(n - 1):
            res += max(0, p[i + 1] - p[i])
        return res
