# https://leetcode.com/problems/number-of-changing-keys/
class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        n = len(s)
        res = 0
        for i in range(1, n):
            if s[i] != s[i - 1]:
                res += 1
        return res
