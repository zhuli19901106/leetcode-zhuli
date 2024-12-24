# medium
# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
# Runtime: 28 ms, faster than 97.68% of Python3 online submissions for Check If Word Is Valid After Substitutions.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Check If Word Is Valid After Substitutions.
import re

class Solution:
    def isValid(self, S: str) -> bool:
        s = S
        while True:
            s1 = re.sub('abc', '', s)
            if s == s1:
                break
            s = s1
        return s == ''
