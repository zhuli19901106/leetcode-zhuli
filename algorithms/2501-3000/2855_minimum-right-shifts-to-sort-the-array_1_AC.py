# easy
# https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if nums[i] < nums[(i + 1) % n]:
                continue
            if res == 0:
                res = n - 1 - i
            else:
                return -1
        return res
