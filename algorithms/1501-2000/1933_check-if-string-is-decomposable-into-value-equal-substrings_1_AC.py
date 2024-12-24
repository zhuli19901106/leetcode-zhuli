# easy
# https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/
# misleading description

class Solution:
    def isDecomposable(self, s: str) -> bool:
        ls = len(s)

        i = 0
        cc2 = 0
        while i < ls:
            j = i + 1
            while j < ls and s[j] == s[i]:
                j += 1
            r = (j - i) % 3
            i = j

            if r == 0:
                continue
            elif r == 1:
                return False
            elif cc2 == 0:
                cc2 += 1
            else:
                return False

        return cc2 == 1
