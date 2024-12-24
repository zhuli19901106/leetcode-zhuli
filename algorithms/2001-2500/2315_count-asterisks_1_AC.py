# easy
# https://leetcode.com/problems/count-asterisks/
class Solution:
    def countAsterisks(self, s: str) -> int:
        fp = 0
        res = 0
        for c in s:
            if c == '|':
                fp = 1 - fp
            elif c == '*':
                res += 1 if fp == 0 else 0
        return res
