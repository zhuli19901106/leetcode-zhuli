# https://leetcode.com/problems/maximum-repeating-substring/
# almost brute force, can be optimized with KMP
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        s, w = sequence, word
        ns, nw = len(s), len(w)
        cc = [0 for i in range(ns)]
        for i in range(nw - 1, ns):
            j = 0
            while j < nw:
                if s[i - j] != w[nw - 1 - j]:
                    break
                j += 1
            if j == nw:
                cc[i] = 1
        for i in range(nw, ns):
            if cc[i] > 0:
                cc[i] += cc[i - nw]
        return max(cc)
