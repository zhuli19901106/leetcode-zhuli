# https://leetcode.com/problems/bitwise-xor-of-all-pairings/
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        res = 0
        if n1 % 2 != 0:
            for x in nums2:
                res ^= x
        if n2 % 2 != 0:
            for x in nums1:
                res ^= x

        return res
