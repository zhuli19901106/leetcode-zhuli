# https://leetcode.com/problems/second-largest-digit-in-a-string/
# 1AC
import re

class Solution:
    def secondHighest(self, s: str) -> int:
        a = sorted(set(list(re.sub(r'\D', '', s))))
        return int(a[-2]) if len(a) >= 2 else -1
