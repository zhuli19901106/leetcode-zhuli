# medium
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
# 1AC, just enumerate
from collections import defaultdict

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_res, max_cc = 0, 0
        mm = [defaultdict(int) for i in range(2)]
        f = 0
        mm[1 - f][0] = 1

        n = len(nums)
        for i, x in enumerate(nums):
            mm[f] = defaultdict(int)
            for k, v in mm[1 - f].items():
                mm[f][k] += mm[1- f][k]
                mm[f][k | x] += mm[1- f][k]
                if (k | x) > max_res:
                    max_res = (k | x)
            f = 1 - f

        return mm[1 - f][max_res]
