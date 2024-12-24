# easy
# https://leetcode.com/problems/special-array-i/
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(1, n):
            if (nums[i] - nums[i - 1]) % 2 == 0:
                return False
        return True
