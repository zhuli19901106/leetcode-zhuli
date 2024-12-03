# https://leetcode.com/problems/split-the-array/
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        mm = {}
        for x in nums:
            if not x in mm:
                mm[x] = 1
            else:
                mm[x] += 1
        return max(mm.values()) <= 2
