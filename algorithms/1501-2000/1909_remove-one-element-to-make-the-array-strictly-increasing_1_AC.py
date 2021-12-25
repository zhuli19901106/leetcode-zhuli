# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/
# a bit tricky

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        cnt = 0
        idx = -1
        for i in range(n - 1):
            if nums[i] >= nums[i + 1]:
                cnt += 1
                idx = i
        if cnt > 1:
            return False
        elif cnt < 1:
            return True
        elif idx == 0 or idx == n - 2:
            return True

        if nums[idx] >= nums[idx - 1] and nums[idx] >= nums[idx + 1]:
            if nums[idx - 1] < nums[idx + 1]:
                return True
        if nums[idx + 1] <= nums[idx] and nums[idx + 1] <= nums[idx + 2]:
            if nums[idx] < nums[idx + 2]:
                return True
        return False
