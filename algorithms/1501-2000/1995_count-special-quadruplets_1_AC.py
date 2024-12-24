# easy
# https://leetcode.com/problems/count-special-quadruplets/
# 1AC, not quite efficient
from collections import defaultdict
from copy import deepcopy

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        m2 = [defaultdict(int)]
        for i in range(1, n):
            m2.append(deepcopy(m2[-1]))
            for j in range(i):
                m2[-1][nums[i] + nums[j]] += 1

        res = 0
        for i in range(3, n):
            for j in range(2, i):
                dt = nums[i] - nums[j]
                if dt in m2[j - 1]:
                    res += m2[j - 1][dt]
        return res
