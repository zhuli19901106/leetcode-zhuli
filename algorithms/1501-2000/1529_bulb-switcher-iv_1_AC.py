# https://leetcode.com/problems/bulb-switcher-iv/
# 1AC
class Solution:
    def minFlips(self, target: str) -> int:
        s = target
        n = len(s)
        i = 0
        while i < n and s[i] == '0':
            i += 1
        res = 0
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            i = j
            res += 1
        return res
