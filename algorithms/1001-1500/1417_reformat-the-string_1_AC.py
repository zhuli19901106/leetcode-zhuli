# https://leetcode.com/problems/reformat-the-string/
# 1AC, string manipulation
class Solution:
    def reformat(self, s: str) -> str:
        s1 = []
        s2 = []
        for c in s:
            if c.isalpha():
                s1.append(c)
            elif c.isdigit():
                s2.append(c)
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        if len(s1) - len(s2) > 1:
            return ''
        res = [0 for i in range(len(s1) + len(s2))]
        res[::2] = s1[:]
        res[1::2] = s2[:]
        return ''.join(res)
