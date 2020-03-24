# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        us = {}
        nc = len(matrix[0])
        mask = (1 << nc) - 1
        for row in matrix:
            val = 0
            for bit in row:
                val = (val << 1) + bit
            if val in us:
                us[val] += 1
            else:
                us[val] = 1
        res = 0
        for k, v in us.items():
            if mask - k in us:
                res = max(res, v + us[mask - k])
            else:
                res = max(res, v)
        return res
