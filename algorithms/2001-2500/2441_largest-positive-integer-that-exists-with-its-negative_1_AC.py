# easy
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        st = set(nums)
        res = -1
        for x in nums:
            if x <= 0 or not -x in st:
                continue
            if res == -1 or res < x:
                res = x
        return res
