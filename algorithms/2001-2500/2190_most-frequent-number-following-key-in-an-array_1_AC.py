# easy
# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/
from collections import defaultdict

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        mm = defaultdict(lambda: 0)
        n = len(nums)
        for i in range(n - 1):
            if nums[i] != key:
                continue
            mm[nums[i + 1]] += 1

        max_val, max_cc = -1, -1
        for val, cc in mm.items():
            if cc > max_cc:
                max_val, max_cc = val, cc

        return max_val
