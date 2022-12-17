# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
class Solution:
    MOD = 10 ** 9 + 7

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sm = []
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                sm.append(cur)
        sm.sort()

        res = 0
        for i in range(left - 1, right):
            res = (res + sm[i]) % self.MOD

        return res
