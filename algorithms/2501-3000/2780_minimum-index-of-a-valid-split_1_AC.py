# https://leetcode.com/problems/minimum-index-of-a-valid-split/
# O(n) for finding dominant, O(1) for checking dominace at any index
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        mm = {}
        for x in nums:
            if not x in mm:
                mm[x] = 1
            else:
                mm[x] += 1

        dom, dom_cc = -1, -1
        for x, cc in mm.items():
            if cc > dom_cc:
                dom, dom_cc = x, cc

        # make sure each checking is O(1) for efficiency
        n = len(nums)
        cc = 0
        for i, x in enumerate(nums):
            if x == dom:
                cc += 1
            if cc * 2 > i + 1 and (dom_cc - cc) * 2 > n - i - 1:
                return i
        return -1
