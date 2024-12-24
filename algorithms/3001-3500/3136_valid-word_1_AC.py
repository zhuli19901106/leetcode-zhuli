# easy
# https://leetcode.com/problems/valid-word/
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowel = set('aeiou')
        cv, cc = 0, 0
        for c in word.lower():
            if c.isdigit():
                continue
            elif c.isalpha():
                if c in vowel:
                    cv += 1
                else:
                    cc += 1
            else:
                return False
        return cv >= 1 and cc >= 1
