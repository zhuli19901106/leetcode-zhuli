# https://leetcode.com/problems/valid-mountain-array/
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        i = 0
        while i + 1 < n:
            if A[i] > A[i + 1]:
                break
            elif A[i] == A[i + 1]:
                return False
            i += 1
        if i == 0 or i + 1 == n:
            return False
        while i + 1 < n:
            if A[i] <= A[i + 1]:
                break
            i += 1
        return i + 1 == n
