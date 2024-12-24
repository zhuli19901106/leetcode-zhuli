# medium
# https://leetcode.com/problems/peak-index-in-a-mountain-array/
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        n = len(A)
        for i in range(1, n - 1):
            if A[i] > A[i - 1] and A[i] > A[i + 1]:
                return i
