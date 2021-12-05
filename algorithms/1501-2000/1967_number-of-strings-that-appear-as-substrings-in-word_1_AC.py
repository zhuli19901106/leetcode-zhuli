# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
# 1AC

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for p in patterns:
            if word.find(p) != -1:
                res += 1
        return res
