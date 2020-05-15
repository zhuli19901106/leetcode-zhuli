import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-z0-9]', '', s.lower())
        n = len(s)
        i = 0
        while i < n - 1 - i:
            if s[i] != s[n - 1 - i]:
                return False
            i += 1
        return True
