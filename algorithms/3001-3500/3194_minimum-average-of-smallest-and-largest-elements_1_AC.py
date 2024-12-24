# easy
# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        i, j = 0, n - 1

        min_ave = nums[n - 1]
        while i < j:
            min_ave = min(min_ave, (nums[i] + nums[j]) / 2)
            i += 1
            j -= 1
        return min_ave
