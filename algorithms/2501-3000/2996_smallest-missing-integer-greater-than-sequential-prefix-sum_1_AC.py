# easy
# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/
# simply terrible
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sm = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1:
                break
            sm += nums[i]

        st = set(nums)
        while sm in st:
            sm += 1
        return sm
