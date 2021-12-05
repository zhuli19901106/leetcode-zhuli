# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/
# 1AC, simulation

class Solution:
    def minTimeToType(self, word: str) -> int:
        res = 0
        x = 0
        for c in word:
            i = ord(c) - ord('a')
            res += min((i + 26 - x) % 26, (x + 26 - i) % 26) + 1
            x = i
        return res
