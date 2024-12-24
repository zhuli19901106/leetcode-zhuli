# medium
# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
# turned on copilot and it did everything with one tab
# had to turn it off immediately
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        mm = {}
        for w, h in rectangles:
            d = self.gcd(w, h)
            tp = (w // d, h // d)
            if not tp in mm:
                mm[tp] = 0
            mm[tp] += 1

        res = 0
        for cc in mm.values():
            res += cc * (cc - 1) // 2
        return res

    def gcd(self, x, y):
        while y != 0:
            x, y = y, x % y

        return x
