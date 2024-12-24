# medium
# https://leetcode.com/problems/vowels-of-all-substrings/
# how many times does one letter appear in all substrings?
class Solution:
    def countVowels(self, word: str) -> int:
        vw = set('aeiou')
        n = len(word)

        res = 0
        for i, c in enumerate(word):
            if not c in vw:
                continue
            res += (i + 1) * (n - i)
        return res
