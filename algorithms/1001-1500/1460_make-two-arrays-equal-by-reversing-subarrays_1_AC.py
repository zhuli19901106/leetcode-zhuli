# easy
# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/
# 1AC, order is irrelevant
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(arr) == sorted(target)
