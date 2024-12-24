# medium
# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # max subarray
        max_sm, sm = 0, 0
        for x in nums:
            sm += x
            if sm < 0:
                sm = 0
            else:
                max_sm = max(max_sm, sm)

        # min subarray
        min_sm, sm = 0, 0
        for x in nums:
            sm += x
            if sm > 0:
                sm = 0
            else:
                min_sm = min(min_sm, sm)

        return max(max_sm, -min_sm)
