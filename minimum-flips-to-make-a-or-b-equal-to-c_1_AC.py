# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
# man, that's rather bitwise.
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        def countOne(x):
            cnt = 0
            while x != 0:
                x = (x & x - 1)
                cnt += 1
            return cnt

        x = a | b
        x1 = a & b
        x2 = a ^ b
        y = x ^ c
        y1 = y & x1
        y2 = y & x2
        y3 = y & c
        return 2 * countOne(y1) + countOne(y2) + countOne(y3)
