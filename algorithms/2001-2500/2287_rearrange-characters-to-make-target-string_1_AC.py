# easy
# https://leetcode.com/problems/rearrange-characters-to-make-target-string/
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        def countChars(s):
            mm = {}
            for c in s:
                if c in mm:
                    mm[c] += 1
                else:
                    mm[c] = 1
            return mm

        ms = countChars(s)
        mt = countChars(target)
        res = len(s) // len(target) + 1
        for c in mt:
            res = min(res, ms.get(c, 0) // mt[c])

        return res
