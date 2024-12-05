# https://leetcode.com/problems/score-of-a-string/
class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(1, n):
            res += abs(ord(s[i]) - ord(s[i - 1]))
        return res
