# easy
# https://leetcode.com/problems/number-of-valid-words-in-a-sentence/
# that's boring
import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        res = 0
        for w in sentence.split():
            if re.match(r'^([a-zA-Z]+\-)?[a-zA-Z]+[!\.,]?$', w):
                res += 1
            if re.match('^[!\.,]$', w):
                res += 1
        return res
