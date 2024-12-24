# medium
# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/
# brute-force

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1

        if cost2 == 0:
            return -1

        res = 0
        for i in range(total // cost1 + 1):
            res += (total - i * cost1) // cost2 + 1

        return res
