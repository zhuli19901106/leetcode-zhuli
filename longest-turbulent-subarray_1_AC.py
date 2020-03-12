# https://leetcode.com/problems/longest-turbulent-subarray/
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        a = []
        n = len(A)
        for i in range(n - 1):
            if A[i] < A[i + 1]:
                a.append(+1)
            elif A[i] > A[i + 1]:
                a.append(-1)
            else:
                a.append(0)
        n = len(a)
        res = 1
        i = 0
        while i < n:
            if a[i] == 0:
                i += 1
                continue
            j = i + 1
            while j < n and a[j] != 0 and a[j] != a[j - 1]:
                j += 1
            res = max(res, j - i + 1)
            i = j
        return res
