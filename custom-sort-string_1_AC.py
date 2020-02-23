# https://leetcode.com/problems/custom-sort-string/
# Runtime: 20 ms, faster than 97.59% of Python3 online submissions for Custom Sort String.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Custom Sort String.
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        ms = {}
        for i, c in enumerate(S):
            ms[c] = i
        ls = len(S)
        a = []
        res = []
        for c in T:
            if c in ms:
                a.append(ms[c])
            else:
                res.append(c)
        a.sort()
        for i in a:
            res.append(S[i])
        res = ''.join(res)
        return res
