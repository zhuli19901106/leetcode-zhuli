# easy
# https://leetcode.com/problems/find-common-elements-between-two-arrays/
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st1 = set(nums1)
        st2 = set(nums2)
        return [len([x for x in nums1 if x in st2]), len([x for x in nums2 if x in st1])]
