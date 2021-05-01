# https://leetcode.com/problems/maximum-ice-cream-bars/
# 1AC, medium?
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for x in costs:
            if coins >= x:
                coins -= x
                res += 1
            else:
                break
        return res
