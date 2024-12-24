# easy
# https://leetcode.com/problems/maximum-population-year/
# 1AC, can be optimized with BIT

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        MIN_Y = 1950
        MAX_Y = 2050
        ap = [0 for i in range(MAX_Y - MIN_Y + 1)]
        for yb, yd in logs:
            for x in range(yb - MIN_Y, yd - MIN_Y):
                ap[x] += 1
        max_i, max_x = 0, 0
        for i, x in enumerate(ap):
            if x > max_x:
                max_i, max_x = i, x
        return max_i + MIN_Y
