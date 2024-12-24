# easy
# https://leetcode.com/problems/consecutive-characters/
# 1AC
class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)
        res = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            res = max(res, j - i)
            i = j
        return res
