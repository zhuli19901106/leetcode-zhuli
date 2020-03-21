# https://leetcode.com/problems/maximum-sum-circular-subarray/
# simple idea, manual labor
class Solution:
    INT_MIN = -(2 ** 31)

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        a = A
        n = len(a)
        if n == 0:
            return 0
        res = self.maxSubarraySingle(a)
        res = max(res, self.maxSubarrayTwoWay(a))
        return res

    def maxSubarrayTwoWay(self, a):
        n = len(a)

        ap1 = [0 for i in range(n)]
        ap1[0] = ps = a[0]
        for i in range(1, n):
            ps += a[i]
            ap1[i] = max(ap1[i - 1], ps)

        ap2 = [0 for i in range(n)]
        ap2[n - 1] = ps = a[n - 1]
        for i in range(n - 2, -1, -1):
            ps += a[i]
            ap2[i] = max(ap2[i + 1], ps)

        res = Solution.INT_MIN
        for i in range(n - 1):
            res = max(res, ap1[i] + ap2[i + 1])
        return res

    def maxSubarraySingle(self, a):
        n = len(a)
        max_sm = Solution.INT_MIN
        sm = 0
        for x in a:
            sm += x
            max_sm = max(max_sm, sm)
            sm = max(sm, 0)
        return max_sm
