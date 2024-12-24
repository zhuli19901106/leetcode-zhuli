# medium
# https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/
# 1AC, count it

from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mm = defaultdict(int)
        for c in s:
            mm[c] += 1

        res = len(s)
        for k, v in mm.items():
            res += v * (v - 1) // 2

        return res
