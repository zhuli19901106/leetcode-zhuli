# easy
# https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
# use regex
import re

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        s = ''.join([chr(x) for x in arr])
        return re.search(r'(.{{{}}})\1{{{}}}'.format(m, k - 1), s) is not None
