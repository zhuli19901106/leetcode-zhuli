# https://leetcode.com/problems/sum-of-all-subset-xor-totals/
# 1AC, brute-force, just iterate
from collections import defaultdict

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 0:
            return 0

        mm = defaultdict(lambda: 0)
        mm[0] += 1

        for i in range(n):
            mm1 = defaultdict(lambda: 0)
            for k, v in mm.items():
                mm1[k] += mm[k]
                mm1[k ^ nums[i]] += mm[k]
            mm = mm1

        res = 0
        for k, v in mm.items():
            res += k * v
        return res
