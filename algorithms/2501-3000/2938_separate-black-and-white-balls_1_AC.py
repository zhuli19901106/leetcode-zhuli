# https://leetcode.com/problems/separate-black-and-white-balls/
# only move 0s and ignore 1s (vice versa)
class Solution:
    def minimumSteps(self, s: str) -> int:
        # move 0 to the left
        res = 0
        j = 0
        for i, c in enumerate(s):
            if c == '0':
                res += i - j
                j += 1
        return res
