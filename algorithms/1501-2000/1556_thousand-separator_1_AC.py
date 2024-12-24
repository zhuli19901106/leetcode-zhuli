# easy
# https://leetcode.com/problems/thousand-separator/
# 1AC
import re

class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        nr = len(s) % 3
        nr = nr if nr != 0 else 3
        s0, s1 = s[:nr], s[nr:]
        if len(s1) > 0:
            s1 = re.sub(r'(\d{3})', r'.\1', s1)
        return s0 + s1
