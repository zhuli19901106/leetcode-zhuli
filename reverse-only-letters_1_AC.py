# https://leetcode.com/problems/reverse-only-letters/
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        a = list(S)
        n = len(a)
        i = 0
        j = n - 1
        while i < j:
            if not a[i].isalpha():
                i += 1
                continue
            if not a[j].isalpha():
                j -= 1
                continue
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        return ''.join(a)
