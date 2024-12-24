# easy
# https://leetcode.com/problems/permutation-difference-between-two-strings/
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ms, mt = {}, {}
        for i, c in enumerate(s):
            ms[c] = i
        for i, c in enumerate(t):
            mt[c] = i

        res = 0
        for c in ms.keys():
            res += abs(ms[c] - mt[c])
        return res
