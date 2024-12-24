# easy
# https://leetcode.com/problems/maximum-number-of-pairs-in-array/
from collections import defaultdict

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        mm = defaultdict(lambda: 0)
        for x in nums:
            mm[x] += 1

        cc = 0
        n = len(nums)
        for k, v in mm.items():
            if v % 2 == 1:
                cc += 1
        res = [(n - cc) // 2, cc]
        return res
