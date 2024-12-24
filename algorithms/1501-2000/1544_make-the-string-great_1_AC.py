# easy
# https://leetcode.com/problems/make-the-string-great/
# 1AC, simulation
class Solution:
    def makeGood(self, s: str) -> str:
        while True:
            s1 = []
            n = len(s)
            i = 0
            while i < n:
                if i + 1 < n and s[i] != s[i + 1] and \
                    s[i].lower() == s[i + 1].lower():
                    i += 2
                    continue
                s1.append(s[i])
                i += 1
            s1 = ''.join(s1)
            if len(s1) == len(s):
                return s1
            s = s1
        # dead code
        return s
