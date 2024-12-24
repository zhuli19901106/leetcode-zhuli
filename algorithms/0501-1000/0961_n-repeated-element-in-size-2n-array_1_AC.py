# easy
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        n = len(A)
        for i in range(n):
            if A[i] == A[(i + 1) % n]:
                return A[i]
        if A[0] != A[1]:
            A[0], A[1] = A[1], A[0]
        for i in range(n):
            if A[i] == A[(i + 1) % n]:
                return A[i]
