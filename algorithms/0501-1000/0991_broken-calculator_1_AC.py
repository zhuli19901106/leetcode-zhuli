# medium
# https://leetcode.com/problems/broken-calculator/
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        x, y = X, Y
        if x >= y:
            return x - y
        res = 0
        while x < y:
            if y % 2 == 0:
                y //= 2
            else:
                y += 1
            res += 1
        res += x - y
        return res
