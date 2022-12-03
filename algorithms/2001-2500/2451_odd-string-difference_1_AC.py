# https://leetcode.com/problems/odd-string-difference/
from collections import defaultdict

class Solution:
    def oddString(self, words: List[str]) -> str:
        nw = len(words)
        n = len(words[0])
        res = -1
        for i in range(n - 1):
            mm = defaultdict(lambda: [])
            for j in range(nw):
                val = ord(words[j][i + 1]) - ord(words[j][i])
                mm[val].append(j)
            if len(mm) == 1:
                continue
            for k, v in mm.items():
                if len(v) == 1:
                    return words[v[0]]

        return None
