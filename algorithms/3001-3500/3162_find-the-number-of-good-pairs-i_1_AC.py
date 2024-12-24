# easy
# https://leetcode.com/problems/find-the-number-of-good-pairs-i/
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1, n2 = len(nums1), len(nums2)
        res = 0
        for i in range(n1):
            for j in range(n2):
                if nums1[i] % (k * nums2[j]) == 0:
                    res += 1
        return res
