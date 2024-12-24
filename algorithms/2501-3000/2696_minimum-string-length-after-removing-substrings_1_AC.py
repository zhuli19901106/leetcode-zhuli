# easy
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
import re

class Solution:
    def minLength(self, s: str) -> int:
        while True:
            update = False

            s1 = re.sub('AB', '', s)
            if len(s1) < len(s):
                s = s1
                update = True
            s1 = re.sub('CD', '', s)
            if len(s1) < len(s):
                s = s1
                update = True

            if not update:
                break

        return len(s)
