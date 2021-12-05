# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
# 1AC, count as you go
from collections import defaultdict

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        mm = defaultdict(int)
        res = 0
        for x in nums:
            if x - k in mm:
                res += mm[x - k]
            if x + k in mm:
                res += mm[x + k]
            mm[x] += 1
        return res
