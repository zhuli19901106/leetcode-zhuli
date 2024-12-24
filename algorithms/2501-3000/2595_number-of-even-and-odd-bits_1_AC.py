# easy
# https://leetcode.com/problems/number-of-even-and-odd-bits/
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        c0, c1 = 0, 0
        even = True
        while n != 0:
            b = (n & 1)
            n >>= 1
            if b == 0:
                even = not even
                continue

            if even:
                c0 += 1
            else:
                c1 += 1
            even = not even

        return [c0, c1]
