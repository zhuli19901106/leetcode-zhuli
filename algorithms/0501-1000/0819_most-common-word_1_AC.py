# easy
# https://leetcode.com/problems/most-common-word/
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        par = re.sub('[^a-z ]', ' ', paragraph.lower())
        aw = par.strip().split()
        wc = {}
        for w in aw:
            if w in ban:
                continue
            if w in wc:
                wc[w] += 1
            else:
                wc[w] = 1
        max_w, max_c = '', -1
        for w, c in wc.items():
            if c > max_c:
                max_w, max_c = w, c
        return max_w
