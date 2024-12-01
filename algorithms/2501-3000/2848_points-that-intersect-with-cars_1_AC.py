# https://leetcode.com/problems/points-that-intersect-with-cars/
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        res = 0
        ll, rr = nums[0]

        n = len(nums)
        for i in range(1, n):
            if rr < nums[i][0]:
                res += rr - ll + 1
                ll, rr = nums[i]
            else:
                rr = max(rr, nums[i][1])
        res += rr - ll + 1
        return res
