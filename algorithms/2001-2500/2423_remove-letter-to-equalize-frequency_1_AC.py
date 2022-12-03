# https://leetcode.com/problems/remove-letter-to-equalize-frequency/
from collections import defaultdict

class Solution:
    def equalFrequency(self, word: str) -> bool:
        mm = defaultdict(lambda: 0)
        for c in word:
            mm[c] += 1
        freq = sorted(mm.values())

        if len(freq) < 2:
            return True

        return (freq[0] == freq[-2] and freq[-2] == freq[-1] - 1) or \
            (freq[0] == 1 and freq[1] == freq[-1])
