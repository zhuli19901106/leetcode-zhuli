# easy
# https://leetcode.com/problems/water-bottles/
# 1AC, simulation
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        nw, nb = numBottles, 0
        res = 0
        while nw > 0 or nb >= numExchange:
            res += nw
            nb += nw
            nw = nb // numExchange
            nb = nb % numExchange
        return res
