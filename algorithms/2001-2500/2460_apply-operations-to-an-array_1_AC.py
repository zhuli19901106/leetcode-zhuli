# easy
# https://leetcode.com/problems/apply-operations-to-an-array/
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        a = nums[:]
        n = len(a)

        for i in range(n - 1):
            if a[i] == a[i + 1]:
                a[i] *= 2
                a[i + 1] = 0
        i, j = 0, 0
        while i < n:
            if a[i] != 0:
                a[j] = a[i]
                j += 1
            i += 1
        while j < n:
            a[j] = 0
            j += 1

        return a
