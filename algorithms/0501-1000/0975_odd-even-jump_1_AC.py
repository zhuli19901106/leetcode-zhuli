# hard
# https://leetcode.com/problems/odd-even-jump/
# tree map, memorized search, use SortedDict in python
from sortedcontainers import SortedDict

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        INT_MIN = -(2 ** 31)
        INT_MAX = 2 ** 31 - 1

        a = A
        n = len(a)

        mm = SortedDict()
        oj = [-1 for i in range(n)]
        for i in range(n - 1, 0, -1):
            mm[a[i]] = i
            j = mm.bisect_left(a[i - 1])
            if j == len(mm):
                continue
            j = mm.iloc[j]
            oj[i - 1] = mm[j]

        mm = SortedDict()
        ej = [-1 for i in range(n)]
        for i in range(n - 1, 0, -1):
            mm[a[i]] = i
            j = mm.bisect_right(a[i - 1]) - 1
            if j == -1:
                continue
            j = mm.iloc[j]
            ej[i - 1] = mm[j]

        dp = {}
        def dfs(idx, odd):
            nonlocal dp

            if idx == n - 1:
                return True
            if (idx, odd) in dp:
                return dp[(idx, odd)]
            idx1 = oj[idx] if odd else ej[idx]
            if idx1 == -1:
                dp[(idx, odd)] = False
            else:
                dp[(idx, odd)] = dfs(idx1, not odd)
            return dp[(idx, odd)]

        res = 0
        for i in range(n):
            if dfs(i, True):
                res += 1
        return res
