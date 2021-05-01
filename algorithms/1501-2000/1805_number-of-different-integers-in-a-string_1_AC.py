# https://leetcode.com/problems/number-of-different-integers-in-a-string/
import re

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = re.sub(r'\D+', ' ', word)
        a = [int(x) for x in s.strip().split()]
        return len(set(a))
