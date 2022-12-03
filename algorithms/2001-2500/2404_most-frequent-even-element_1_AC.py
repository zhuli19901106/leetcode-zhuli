# https://leetcode.com/problems/most-frequent-even-element/
from collections import defaultdict

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mm = defaultdict(lambda: 0)
        for x in nums:
            mm[x] += 1
        a = sorted(mm.items(), key=lambda x: (-x[1], x[0]))
        for k, v in a:
            if k % 2 == 0:
                return k
        return -1
