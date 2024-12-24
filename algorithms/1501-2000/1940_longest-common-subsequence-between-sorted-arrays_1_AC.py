# medium
# https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/
# 1AC, merge them

class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        n = len(arrays)
        alen = [i for i in range(n)]
        alen.sort(key=lambda x: len(arrays[x]))

        res = arrays[alen[0]]
        for i in range(1, n):
            res = self.mergeArray(res, arrays[alen[i]])
        return res

    def mergeArray(self, a1, a2):
        n1, n2 = len(a1), len(a2)
        if n1 == 0 or n2 == 0:
            return []
        if a1[-1] < a2[0] or a2[-1] < a1[0]:
            return []

        res = []
        i1, i2 = 0, 0
        while i1 < n1 and i2 < n2:
            if a1[i1] < a2[i2]:
                i1 += 1
            elif a1[i1] > a2[i2]:
                i2 += 1
            else:
                res.append(a1[i1])
                i1 += 1
                i2 += 1
        return res
