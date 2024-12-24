# easy
# https://leetcode.com/problems/duplicate-zeros/
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        a = arr
        n = len(a)
        z = 0
        for i in range(n):
            if a[i] == 0:
                z += 1
        for i in range(n - 1, -1, -1):
            if a[i] == 0:
                z -= 1
            j = i + z
            if j < n:
                a[j] = a[i]
            if a[i] == 0 and j + 1 < n:
                a[j + 1] = a[i]
