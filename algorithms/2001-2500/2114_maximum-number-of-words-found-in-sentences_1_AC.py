# easy
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
# 1AC, one-liner

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(sen.split()) for sen in sentences])
