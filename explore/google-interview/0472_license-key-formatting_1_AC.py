# https://leetcode.com/explore/interview/card/google/67/sql-2/472/
import re

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = re.sub('-', '', S)
        n = len(s)
        r = n % K
        res = [s[:r]] if r > 0 else []
        res += [s[r + i * K: r + (i + 1) * K] for i in range(n // K)]
        return ('-'.join(res)).upper()
