# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
# 1AC

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if self.isPal(w):
                return w
        return ''

    def isPal(self, s):
        ls = len(s)
        if ls <= 1:
            return True
        i = 0
        while i < ls - 1 - i:
            if s[i] != s[ls - 1 - i]:
                return False
            i += 1
        return True
