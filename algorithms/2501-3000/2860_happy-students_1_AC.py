# medium
# https://leetcode.com/problems/happy-students/
# very puzzling description
# a ridiculously tricky question
class Solution:
    def countWays(self, nums: List[int]) -> int:
        # there's only one boundary, think about it
        nums.sort()

        n = len(nums)
        res = 0
        for i, x in enumerate(nums):
            if i + 1 <= x:
                continue
            if i < n - 1 and i + 1 >= nums[i + 1]:
                continue
            res += 1

        if nums[0] > 0:
            # select no one
            res += 1

        return res
