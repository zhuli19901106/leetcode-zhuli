# hard
# https://leetcode.com/problems/split-array-largest-sum/
# binary search on partition
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        ll, rr = max(nums), sum(nums)
        if self.partition(nums, ll) <= k:
            return ll
        if self.partition(nums, rr) >= k:
            return rr

        while rr - ll > 1:
            mm = ll + (rr - ll >> 1)
            cc = self.partition(nums, mm)
            if cc > k:
                ll = mm
            else:
                rr = mm
        return rr

    def partition(self, nums, x):
        n = len(nums)
        cc = 1
        sm = 0
        for i in range(n):
            sm += nums[i]
            if sm > x:
                cc += 1
                sm = nums[i]
        return cc
