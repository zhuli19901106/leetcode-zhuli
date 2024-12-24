# easy
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
import re

class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = S
        while True:
            s1 = self.dedup(s)
            if s == s1:
                break
            else:
                s = s1
        return s

    def dedup(self, s):
        pat = '(.)\\1{1}'
        return re.sub(pat, '', s)
