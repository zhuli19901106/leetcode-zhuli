# easy
# https://leetcode.com/problems/binary-gap/
class Solution:
    def binaryGap(self, N: int) -> int:
        n = N
        p1 = -1
        p2 = 0
        res = 0
        while n != 0:
            if (n & 1) == 1:
                if p1 != -1:
                    res = max(res, p2 - p1)
                p1 = p2
            n >>= 1
            p2 += 1
        return res
