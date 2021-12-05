# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
# 1AC
from collections import defaultdict

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        mc = defaultdict(int)
        nw = len(words)
        for w in words:
            for c in w:
                mc[c] += 1
        for k, v in mc.items():
            if v % nw != 0:
                return False
        return True
