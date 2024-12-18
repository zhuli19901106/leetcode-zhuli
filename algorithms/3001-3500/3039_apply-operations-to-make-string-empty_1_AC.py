# https://leetcode.com/problems/apply-operations-to-make-string-empty/
# just record the last occurrence of each char
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        mm = {}
        pos = {}
        for i, c in enumerate(s):
            if not c in mm:
                mm[c] = 0
            mm[c] += 1
            pos[c] = i

        max_cc = max(mm.values())
        a = [(pos[c], c) for c, cc in mm.items() if cc == max_cc]
        a.sort()

        res = ''.join([c for _, c in a])
        return res
