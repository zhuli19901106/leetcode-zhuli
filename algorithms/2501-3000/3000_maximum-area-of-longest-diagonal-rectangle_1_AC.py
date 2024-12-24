# easy
# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = (-1, -1)
        for w, h in dimensions:
            d2, a = w * w + h * h, w * h
            if (d2, a) > res:
                res = (d2, a)
        return res[1]
