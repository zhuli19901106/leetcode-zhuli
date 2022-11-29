# https://leetcode.com/problems/divide-array-into-equal-pairs/
from collections import defaultdict

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False

        mm = defaultdict(lambda: 0)
        for x in nums:
            mm[x] += 1
        for k, v in mm.items():
            if v % 2 != 0:
                return False
        return True
