# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        i1, i2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        while i1 < n1 or i2 < n2:
            if i1 == n1:
                res.append(nums2[i2][:])
                i2 += 1
            elif i2 == n2:
                res.append(nums1[i1][:])
                i1 += 1
            elif nums1[i1][0] < nums2[i2][0]:
                res.append(nums1[i1][:])
                i1 += 1
            elif nums1[i1][0] > nums2[i2][0]:
                res.append(nums2[i2][:])
                i2 += 1
            else:
                res.append([nums1[i1][0], nums1[i1][1] + nums2[i2][1]])
                i1 += 1
                i2 += 1
        return res
