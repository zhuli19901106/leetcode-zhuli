# https://leetcode.com/problems/percentage-of-letter-in-string/
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cc = 0
        for c in s:
            if c == letter:
                cc += 1
        return int(cc / len(s) * 100.0)
