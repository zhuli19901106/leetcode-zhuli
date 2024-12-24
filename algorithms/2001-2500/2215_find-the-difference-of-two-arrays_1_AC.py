# easy
# https://leetcode.com/problems/find-the-difference-of-two-arrays/
from collections import defaultdict

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        m1 = defaultdict(lambda: 0)
        for x in nums1:
            m1[x] += 1
        m2 = defaultdict(lambda: 0)
        for x in nums2:
            m2[x] += 1

        a1 = set()
        for x in nums1:
            if x in nums2:
                continue
            a1.add(x)
        a2 = set()
        for x in nums2:
            if x in nums1:
                continue
            a2.add(x)

        return [list(a1), list(a2)]
