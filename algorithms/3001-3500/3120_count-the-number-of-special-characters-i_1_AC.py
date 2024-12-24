# easy
# https://leetcode.com/problems/count-the-number-of-special-characters-i/
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        st = set(word)
        res = 0
        for c in st:
            if c.islower() and c.upper() in st:
                res += 1
        return res
