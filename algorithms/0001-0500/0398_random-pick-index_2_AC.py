# medium
# https://leetcode.com/problems/random-pick-index/
from random import randint

class Solution:

    def __init__(self, nums: List[int]):
        self.mm = {}

        mm = self.mm
        for i, x in enumerate(nums):
            if not x in mm:
                mm[x] = []
            mm[x].append(i)

    def pick(self, target: int) -> int:
        mm = self.mm
        if not target in mm:
            return -1
        return mm[target][randint(0, len(mm[target]) - 1)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)