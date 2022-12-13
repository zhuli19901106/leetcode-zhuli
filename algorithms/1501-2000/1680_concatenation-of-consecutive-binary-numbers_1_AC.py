# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
# don't calculate bit by bit for every number
from math import log2

class Solution:
    MAXN = 10 ** 5
    MOD = 10 ** 9 + 7

    def __init__(self) -> None:
        self.res = [0]

    def concatenatedBinary(self, n: int) -> int:
        i = len(self.res)
        while i <= n:
            nb = int(log2(i)) + 1
            val = ((self.res[i - 1] << nb) + i) % self.MOD
            self.res.append(val)

            i += 1

        return self.res[n]
