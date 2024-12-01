# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return s == ''.join([w[0] for w in words])
