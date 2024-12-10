# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/
class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        i = 0
        a = []
        while i < n:
            j = i + 1
            while j < n and s[i] == s[j]:
                j += 1
            a.append((j - i) & 1)
            i = j

        m = len(a)
        res = 0
        i = 0
        while i < m:
            if not a[i]:
                i += 1
                continue

            if i == m - 1:
                res += a[i]
                i += 1
                continue

            if a[i] & a[i + 1]:
                a[i], a[i + 1] = 0, 0
                res += 1
                i += 2
                continue

            a[i], a[i + 1] = a[i + 1], a[i]
            res += 1
            i += 1
        return res
