# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
# 1AC
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
