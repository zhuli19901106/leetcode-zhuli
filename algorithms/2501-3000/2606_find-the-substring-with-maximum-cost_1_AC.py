# medium
# https://leetcode.com/problems/find-the-substring-with-maximum-cost/
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        MAXC = 26

        mm = {}
        for i in range(MAXC):
            mm[chr(ord('a') + i)] = i + 1
        for i in range(len(chars)):
            mm[chars[i]] = vals[i]

        a = [mm[c] for c in s]

        max_sm = 0
        sm = 0
        for x in a:
            sm += x
            if sm > max_sm:
                max_sm = sm
            if sm < 0:
                sm = 0
        return max_sm
