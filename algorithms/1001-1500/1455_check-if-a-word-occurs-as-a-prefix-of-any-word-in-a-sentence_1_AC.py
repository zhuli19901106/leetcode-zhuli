# easy
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
# 1AC
import re

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, s in enumerate(re.split('\s+', sentence.strip())):
            if s.startswith(searchWord):
                return i + 1
        return -1
