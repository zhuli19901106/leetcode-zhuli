# easy
# https://leetcode.com/problems/determine-if-string-halves-are-alike/
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        st = set('aeiou')
        n = len(s) // 2
        c1, c2 = 0, 0
        s = s.lower()
        for i in range(n):
            if s[i] in st:
                c1 += 1
            if s[i + n] in st:
                c2 += 1
        return c1 == c2
