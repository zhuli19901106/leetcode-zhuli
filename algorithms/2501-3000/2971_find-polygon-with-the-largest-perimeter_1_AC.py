# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/
# should be "easy" once you get it
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = -1

        sm = nums[0] + nums[1]
        for i in range(2, n):
            if nums[i] < sm:
                res = sm + nums[i]
            sm += nums[i]
        return res
