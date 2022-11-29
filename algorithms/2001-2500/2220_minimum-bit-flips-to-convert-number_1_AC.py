# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        diff = start ^ goal
        cnt = 0
        while diff != 0:
            diff &= diff - 1
            cnt += 1
        return cnt
