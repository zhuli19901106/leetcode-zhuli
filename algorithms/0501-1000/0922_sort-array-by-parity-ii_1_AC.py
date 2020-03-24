# https://leetcode.com/problems/sort-array-by-parity-ii/
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A) // 2
        i = 0
        j = 0
        while True:
            while i < n and A[2 * i] % 2 == 0:
                i += 1
            while j < n and A[2 * j + 1] % 2 == 1:
                j += 1
            if i < n and j < n:
                A[2 * i], A[2 * j + 1] = A[2 * j + 1], A[2 * i]
                i += 1
                j += 1
            else:
                break
        return A
