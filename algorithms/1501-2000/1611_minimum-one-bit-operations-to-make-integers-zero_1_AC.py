# hard
# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/
# quite far from intuition, tbh

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        bits = []
        while n != 0:
            bits.append(n & 1)
            n >>= 1
        bits.append(0)

        res = 0
        nb = len(bits)
        sign = 1
        for i in range(nb - 1, -1, -1):
            if bits[i] == 0:
                continue
            res += sign * ((1 << i + 1) - 1)
            sign = -sign

        return res
