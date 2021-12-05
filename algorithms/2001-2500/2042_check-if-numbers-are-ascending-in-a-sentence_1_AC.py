# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/
# 1AC
import re

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(w) for w in s.split() if re.match(r'^\d+$', w)]
        n = len(nums)
        for i in range(n - 1):
            if nums[i] >= nums[i + 1]:
                return False
        return True
