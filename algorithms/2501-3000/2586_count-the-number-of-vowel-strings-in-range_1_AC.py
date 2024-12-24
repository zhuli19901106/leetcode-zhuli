# easy
# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vow = set('aeiou')
        res = 0
        for i in range(left, right + 1):
            if words[i][0] in vow and words[i][-1] in vow:
                res += 1
        return res
