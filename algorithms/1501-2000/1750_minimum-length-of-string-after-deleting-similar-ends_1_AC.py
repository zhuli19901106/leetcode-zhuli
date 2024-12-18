# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
# should be easy
class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)

        i, j = 0, n - 1
        while i < j and s[i] == s[j]:
            c = s[i]

            i1 = i + 1
            while i1 < n and s[i1] == c:
                i1 += 1
            i = i1

            j1 = j - 1
            while j1 > -1 and s[j1] == c:
                j1 -= 1
            j = j1

        return max(j - i + 1, 0)
