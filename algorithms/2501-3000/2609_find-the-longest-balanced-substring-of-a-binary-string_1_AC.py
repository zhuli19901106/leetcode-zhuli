# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        while i < n and s[i] != '0':
            i += 1

        res = 0
        while i < n:
            n0, n1 = 0, 0

            j = i
            while j < n and s[j] == '0':
                j += 1
            n0 = j - i
            i = j

            while j < n and s[j] == '1':
                j += 1
            n1 = j - i
            i = j

            res = max(res, min(n0, n1) * 2)

        return res
