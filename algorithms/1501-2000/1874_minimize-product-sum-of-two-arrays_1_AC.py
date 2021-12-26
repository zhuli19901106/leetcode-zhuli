# https://leetcode.com/problems/minimize-product-sum-of-two-arrays/
# 1AC, a teaser

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        a1 = sorted(nums1)
        a2 = sorted(nums2, reverse=True)
        return sum([a1[i] * a2[i] for i in range(len(a1))])
