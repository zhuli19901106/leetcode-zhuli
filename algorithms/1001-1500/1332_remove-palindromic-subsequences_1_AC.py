# easy
# https://leetcode.com/problems/remove-palindromic-subsequences/
# warning: brain teaser
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0
        def isPal(s):
            ls = len(s)
            i = 0
            j = ls - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        if isPal(s):
            return 1
        return 2
