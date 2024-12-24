# easy
# https://leetcode.com/problems/single-row-keyboard/
# 1AC
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mm = {}
        for i, c in enumerate(keyboard):
            mm[c] = i
        c0 = keyboard[0]
        res = 0
        for c in word:
            res += abs(mm[c] - mm[c0])
            c0 = c
        return res
