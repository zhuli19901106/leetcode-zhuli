# https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/
class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)
        if min_val == max_val:
            return 0
        res = 0
        for x in nums:
            if x > min_val and x < max_val:
                res += 1
        return res
