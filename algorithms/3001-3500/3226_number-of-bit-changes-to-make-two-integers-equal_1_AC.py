# https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if (n & k) != k:
            return -1

        n ^= k
        res = 0
        while n != 0:
            n &= n - 1
            res += 1
        return res
