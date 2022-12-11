# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ti = 0
        ns, nt = len(s), len(t)
        for si in range(ns):
            if ti == nt:
                break
            if s[si] == t[ti]:
                ti += 1

        return nt - ti
