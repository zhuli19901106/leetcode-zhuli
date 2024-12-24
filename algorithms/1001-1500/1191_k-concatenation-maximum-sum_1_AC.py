# medium
# https://leetcode.com/problems/k-concatenation-maximum-sum/
# multiple possible cases
class Solution:
    MOD = 10 ** 9 + 7

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        n = len(arr)

        val = max(arr)
        if val <= 0:
            return 0

        val = min(arr)
        sum_val = sum(arr)
        if val >= 0:
            return (sum_val * k) % Solution.MOD

        while True:
            s1 = self.maxSumSingle(arr)
            res = s1
            if k <= 1:
                break

            s2 = self.maxSumSingle(arr[:] + arr[:])
            res = max(res, s2)
            if k <= 2:
                break

            s3 = (k - 2) * sum_val
            mps = ps = 0
            for i in range(n - 1, -1, -1):
                ps += arr[i]
                mps = max(mps, ps)
            s3 += mps
            mps = ps = 0
            for i in range(n):
                ps += arr[i]
                mps = max(mps, ps)
            s3 += mps
            res = max(res, s3)

            break
        res %= Solution.MOD

        return res

    def maxSumSingle(self, arr):
        max_sm = 0
        sm = 0
        for x in arr:
            sm += x
            max_sm = max(max_sm, sm)
            sm = max(sm, 0)
        return max_sm
