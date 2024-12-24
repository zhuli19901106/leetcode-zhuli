# medium
# https://leetcode.com/problems/water-bottles-ii/
# should totally be "easy"
# considering the data range, just simulate
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0
        while numBottles >= numExchange:
            res += numExchange
            numBottles += 1 - numExchange
            numExchange += 1
        res += numBottles
        numBottles = 0

        return res
