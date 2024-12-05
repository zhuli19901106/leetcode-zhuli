# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/
class Solution:
    def getSmallestString(self, s: str) -> str:
        n = len(s)
        for i in range(n - 1):
            if s[i] > s[ i + 1] and (ord(s[i]) - ord(s[i + 1])) % 2 == 0:
                a = list(s)
                a[i], a[i + 1] = a[i + 1], a[i]
                return ''.join(a)
        return s
