# medium
# https://leetcode.com/problems/minimum-length-of-string-after-operations/
# a teaser
class Solution:
    def minimumLength(self, s: str) -> int:
        mm = {}
        for c in s:
            if not c in mm:
                mm[c] = 0
            mm[c] += 1

        res = 0
        for cc in mm.values():
            res += 1 if cc & 1 == 1 else 2
        return res
