# medium
# https://leetcode.com/problems/convert-to-base-2/
# a bit tricky
class Solution:
    def baseNeg2(self, N: int) -> str:
        n = N
        if n == 0:
            return '0'

        res = []
        while n != 0:
            res.append(chr(ord('0') + (n & 1)))
            # key here
            n = -(n >> 1)
        return ''.join(res[::-1])
