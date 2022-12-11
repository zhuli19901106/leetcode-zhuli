# https://leetcode.com/problems/tuple-with-same-product/
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        mm = {}
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                p = nums[i] * nums[j]
                if p in mm:
                    mm[p] += 1
                else:
                    mm[p] = 1

        res = 0
        for p, cc in mm.items():
            res += 8 * cc * (cc - 1) // 2

        return res
