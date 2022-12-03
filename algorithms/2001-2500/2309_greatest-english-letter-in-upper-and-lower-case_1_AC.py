# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/
from collections import defaultdict

class Solution:
    def greatestLetter(self, s: str) -> str:
        mm = defaultdict(lambda: 0)
        for c in s:
            if c.islower():
                mm[c.upper()] |= 1
            if c.isupper():
                mm[c] |= 2

        ac = sorted(mm.keys(), reverse=True)
        for c in ac:
            if mm[c] == 3:
                return c
        return ''
