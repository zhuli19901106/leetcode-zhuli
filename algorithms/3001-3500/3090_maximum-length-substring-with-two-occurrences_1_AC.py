# easy
# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/
from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = 0
        mm = defaultdict(lambda: 0)

        ll, rr = 0, 0
        n = len(s)
        while rr < n:
            mm[s[rr]] += 1

            if mm[s[rr]] <= 2:
                res = max(res, rr - ll + 1)

            while ll < rr and mm[s[rr]] > 2:
                mm[s[ll]] -= 1
                ll += 1

            rr += 1

        return res
