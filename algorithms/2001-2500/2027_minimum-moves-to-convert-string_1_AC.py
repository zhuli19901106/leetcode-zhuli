# easy
# https://leetcode.com/problems/minimum-moves-to-convert-string/
# 1AC, no-brainer

class Solution:
    def minimumMoves(self, s: str) -> int:
        ls = len(s)
        res = 0
        i = 0
        while i < ls:
            if s[i] == 'X':
                res += 1
                i += 3
            else:
                i += 1
        return res
