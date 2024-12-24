# easy
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
# 1AC, no-brainer

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(2, n):
            if s[i] != s[i - 1] and s[i - 1] != s[i - 2] and s[i] != s[i - 2]:
                res += 1
        return res
