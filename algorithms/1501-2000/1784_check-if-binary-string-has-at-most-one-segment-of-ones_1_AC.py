# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        i = 0
        cc = 0
        while i < n:
            if s[i] != '1':
                i += 1
                continue
            j = i + 1
            while j < n and s[j] == '1':
                j += 1
            cc += 1
            i = j
        return cc <= 1
