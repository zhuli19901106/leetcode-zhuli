# easy
# https://leetcode.com/problems/sort-array-by-parity/
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        i = 0
        j = n - 1
        while i < j:
            if A[i] % 2 == 0:
                i += 1
                continue
            if A[j] % 2 == 1:
                j -= 1
                continue
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        return A
