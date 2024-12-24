# easy
# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        a = sorted(cost, reverse=True)
        n = len(a)

        res = sum(a)
        for i in range(0, n, 3):
            if i + 2 < n:
                res -= a[i + 2]

        return res
