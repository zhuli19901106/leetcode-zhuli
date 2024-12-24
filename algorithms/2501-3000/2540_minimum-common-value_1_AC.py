# easy
# https://leetcode.com/problems/minimum-common-value/
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i1, i2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        while i1 < n1 and i2 < n2:
            if nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:
                return nums1[i1]
        return -1
