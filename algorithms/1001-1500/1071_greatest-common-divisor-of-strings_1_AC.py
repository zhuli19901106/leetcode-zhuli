# https://leetcode.com/problems/greatest-common-divisor-of-strings/
import re

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def match(s, t):
            if re.match(f'^({t})+$', s):
                return True
            return False

        n1 = len(str1)
        n2 = len(str2)
        for nd in range(min(n1, n2), 0, -1):
            if n1 % nd != 0 or n2 % nd != 0:
                continue
            d = str1[:nd]
            if match(str1, d) and match(str2, d):
                return d
        return ''
