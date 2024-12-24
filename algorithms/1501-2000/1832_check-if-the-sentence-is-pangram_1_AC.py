# easy
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/
# 1AC
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence.lower())) == 26
