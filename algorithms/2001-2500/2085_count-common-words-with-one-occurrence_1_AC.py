# easy
# https://leetcode.com/problems/count-common-words-with-one-occurrence/
# 1AC
from collections import defaultdict

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        m1 = defaultdict(int)
        for w in words1:
            m1[w] += 1
        m2 = defaultdict(int)
        for w in words2:
            m2[w] += 1

        res = 0
        for k, v in m1.items():
            if v != 1:
                continue
            if k in m2 and m2[k] == 1:
                res += 1
        return res
