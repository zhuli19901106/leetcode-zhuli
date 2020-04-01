# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/
# 1AC, n pointers, move all forward with bisecting
from bisect import bisect_left
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        a = mat
        n = len(a)
        m = len(a[0])
        ci = [0 for i in range(n)]

        while True:
            for i in range(n):
                if ci[i] == m:
                    return -1

            max_cur = a[0][ci[0]]
            for i in range(1, n):
                max_cur = max(max_cur, a[i][ci[i]])

            mis = []
            for i in range(n):
                if a[i][ci[i]] != max_cur:
                    mis.append(i)
            if len(mis) == 0:
                return max_cur

            for i in mis:
                j = bisect_left(a[i], max_cur)
                ci[i] = j
        return -1
