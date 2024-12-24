# easy
# https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
# 1AC, no brainer
class Solution:
    def modifyString(self, s: str) -> str:
        a = list(s)
        n = len(s)
        for i, c in enumerate(a):
            if c != '?':
                continue
            for j in range(26):
                c1 = chr(ord('a') + j)
                if (i > 0 and c1 == a[i - 1]) or (i < n - 1 and c1 == a[i + 1]):
                    continue
                a[i] = c1
        return ''.join(a)
