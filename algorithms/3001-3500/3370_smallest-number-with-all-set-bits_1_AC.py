# easy
# https://leetcode.com/problems/smallest-number-with-all-set-bits/
class Solution:
    def smallestNumber(self, n: int) -> int:
        while (n & n + 1) != 0:
            n |= n + 1
        return n
