# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
# 1AC, medium?
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        a = arr
        n = len(a)
        df = difference
        mm = {}
        for i in range(n):
            res = mm.get(a[i], 1)
            if a[i] - df in mm:
                res = max(res, mm[a[i] - df] + 1)
            mm[a[i]] = res
        return max(mm.values())
