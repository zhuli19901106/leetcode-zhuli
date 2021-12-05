# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
# 1AC
from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        mm = defaultdict(int)
        for c in s:
            mm[c] += 1
        st = set()
        for v in mm.values():
            st.add(v)
        return len(st) == 1
