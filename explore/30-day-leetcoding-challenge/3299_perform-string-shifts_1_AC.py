# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3299/
# 1AC
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        ls = len(s)
        k = 0
        for dr, am in shift:
            k += (2 * dr - 1) * am
        k %= ls
        k = (ls - k) % ls
        return s[k:] + s[:k]
