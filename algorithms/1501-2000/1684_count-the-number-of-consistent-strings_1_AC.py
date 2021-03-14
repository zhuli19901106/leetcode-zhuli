# https://leetcode.com/problems/count-the-number-of-consistent-strings/
# 1AC
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        sta = set(allowed)
        for w in words:
            f = True
            for c in w:
                if not c in sta:
                    f = False
                    break
            if f:
                res += 1
        return res
