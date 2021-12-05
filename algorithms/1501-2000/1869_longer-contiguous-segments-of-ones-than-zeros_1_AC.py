# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/
# 1AC

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ls = len(s)
        i = 0
        n0, n1 = 0, 0
        while i < ls:
            j = i + 1
            while j < ls and s[j] == s[i]:
                j += 1
            if s[i] == '0':
                n0 = max(n0, j - i)
            else:
                n1 = max(n1, j - i)
            i = j
        return n1 > n0
