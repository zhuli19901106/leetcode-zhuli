# https://leetcode.com/problems/count-substrings-that-differ-by-one-character/
# don't get lost within the loops
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ns = len(s)
        nt = len(t)

        res = 0
        for i in range(ns):
            for j in range(nt):
                k = 0
                df = 0
                while i + k < ns and j + k < nt and df <= 1:
                    if s[i + k] != t[j + k]:
                        df += 1
                    k += 1
                    if df == 1:
                        res += 1
        return res
