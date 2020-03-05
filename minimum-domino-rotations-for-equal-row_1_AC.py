# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        st = set((A[0], B[0]))
        for i in range(1, n):
            st &= set((A[i], B[i]))
            if len(st) == 0:
                break
        st = list(st)
        if len(st) == 0:
            return -1
        x = st[0]
        res1 = res2 = 0
        for i in range(n):
            if A[i] == x and B[i] != x:
                res2 += 1
            elif A[i] != x and B[i] == x:
                res1 += 1
        return min(res1, res2)
