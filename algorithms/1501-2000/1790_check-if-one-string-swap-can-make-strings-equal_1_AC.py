# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
# careful
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        i1 = 0
        while i1 <= n - 1:
            if s1[i1] != s2[i1]:
                break
            else:
                i1 += 1
        if i1 == n:
            return True

        i2 = n - 1
        while i2 >= 0:
            if s1[i2] != s2[i2]:
                break
            else:
                i2 -= 1
        if i2 == i1:
            return False

        for i in range(i1 + 1, i2):
            if s1[i] != s2[i]:
                return False
        return s1[i1] == s2[i2] and s1[i2] == s2[i1]
