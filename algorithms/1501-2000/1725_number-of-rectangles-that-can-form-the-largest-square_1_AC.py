# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
# 1AC
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len, res = 0, 0
        for r in rectangles:
            cur_len = min(r)
            if cur_len > max_len:
                max_len, res = cur_len, 1
            elif cur_len == max_len:
                res += 1
        return res
