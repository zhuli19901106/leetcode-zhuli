# medium
# https://leetcode.com/problems/construct-k-palindrome-strings/
# took me ten minutes to prove it was extremely simple
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        mm = {}
        n = len(s)
        for c in s:
            mm[c] = mm.get(c, 0) + 1
        oc = 0
        for v in mm.values():
            if v % 2 == 1:
                oc += 1
        return k <= n and k >= oc
