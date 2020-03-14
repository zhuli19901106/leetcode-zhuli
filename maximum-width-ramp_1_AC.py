# https://leetcode.com/problems/maximum-width-ramp/
# https://leetcode.com/problems/maximum-width-ramp/discuss/423575/Java-sorting-the-index
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)
        a = [i for i in range(n)]
        a.sort(key=lambda x: A[x])
        res = 0
        max_i = a[n - 1]
        for i in range(n - 2, -1, -1):
            if a[i] <= max_i:
                res = max(res, max_i - a[i])
            else:
                max_i = a[i]
        return res
