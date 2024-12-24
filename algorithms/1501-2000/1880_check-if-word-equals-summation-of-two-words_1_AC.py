# easy
# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
# 1AC

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def numVal(w):
            res = 0
            for c in w:
                res = res * 10 + ord(c) - ord('a')
            return res

        return numVal(firstWord) + numVal(secondWord) == numVal(targetWord)
