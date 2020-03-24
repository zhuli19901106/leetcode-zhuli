# https://leetcode.com/problems/break-a-palindrome/
# what?
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        p = list(palindrome)
        n = len(p)
        if n == 1:
            return ''
        i = 0
        while i < n - 1 - i:
            if p[i] > 'a':
                break
            i += 1
        if i >= n - 1 - i:
            p[-1] = 'b'
        else:
            p[i] = 'a'
        return ''.join(p)
