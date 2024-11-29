# https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        x1 = min(nums1)
        x2 = min(nums2)

        nums1.sort()
        st2 = set(nums2)
        for x in nums1:
            if x in st2:
                return x

        if x1 > x2:
            x1, x2 = x2, x1
        return x1 * 10 + x2 if x1 < x2 else x1
