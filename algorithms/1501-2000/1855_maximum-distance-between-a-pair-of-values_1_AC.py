# medium
# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        i, j = n1 - 1, n2 - 1

        # always keeps i <= j
        while i > j:
            i -= 1

        res = 0
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                res = max(res, j - i)
                i -= 1
            elif i < j:
                j -= 1
            else:
                i -= 1
                j -= 1
        return res
