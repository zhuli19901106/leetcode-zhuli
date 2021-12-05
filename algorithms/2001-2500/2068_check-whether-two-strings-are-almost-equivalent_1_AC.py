# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/
# sloppy
from collections import defaultdict

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        m1, m2 = defaultdict(int), defaultdict(int)
        for c in word1:
            m1[c] += 1
        for c in word2:
            m2[c] += 1

        max_diff = 0
        for i in range(26):
            c = chr(ord('a') + i)
            max_diff = max(max_diff, abs(m1[c] - m2[c]))
        return max_diff <= 3
