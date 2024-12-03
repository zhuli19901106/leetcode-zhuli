# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/
class Solution:
    def minimumPushes(self, word: str) -> int:
        res = 0
        push = 1
        n = len(word)
        while n > 0:
            res += min(n, 8) * push
            n -= min(n, 8)
            push += 1
        return res
