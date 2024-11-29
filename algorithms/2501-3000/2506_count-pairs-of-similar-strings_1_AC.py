# https://leetcode.com/problems/count-pairs-of-similar-strings/
from collections import defaultdict

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        sorted_words = [''.join(sorted(set(w))) for w in words]
        mm = defaultdict(lambda: 0)
        for w in sorted_words:
            mm[w] += 1

        res = 0
        for k, v in mm.items():
            res += v * (v - 1) // 2

        return res
