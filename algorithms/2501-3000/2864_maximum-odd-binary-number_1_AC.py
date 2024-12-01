# https://leetcode.com/problems/maximum-odd-binary-number/
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n0, n1 = 0, 0
        for c in s:
            if c == '0':
                n0 += 1
            else:
                n1 += 1
        return ''.join(['1' for _ in range(n1 - 1)] + ['0' for _ in range(n0)] + ['1'])
