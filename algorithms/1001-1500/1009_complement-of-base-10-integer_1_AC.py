# easy
# https://leetcode.com/problems/complement-of-base-10-integer/
from math import floor, log2

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        return (1 << int(floor(log2(N)) + 1)) - 1 - N
