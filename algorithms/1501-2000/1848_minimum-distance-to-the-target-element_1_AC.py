# https://leetcode.com/problems/minimum-distance-to-the-target-element/
# 1AC
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        for i in range(max(start + 1, n - start)):
            if start - i >= 0 and nums[start - i] == target:
                return i
            if start + i <= n - 1 and nums[start + i] == target:
                return i
        return -1
