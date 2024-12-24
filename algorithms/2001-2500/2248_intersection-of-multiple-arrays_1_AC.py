# easy
# https://leetcode.com/problems/intersection-of-multiple-arrays/
from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        mm = defaultdict(lambda: 0)
        for a in nums:
            for x in a:
                mm[x] += 1

        res = []
        na = len(nums)
        for k, v in mm.items():
            if v == na:
                res.append(k)
        res.sort()
        return res
