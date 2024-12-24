# easy
# https://leetcode.com/problems/delete-columns-to-make-sorted/
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n = len(A)
        m = len(A[0])
        count = 0
        for i in range(m):
            j = 0
            while j < n - 1:
                if A[j][i] > A[j + 1][i]:
                    break
                j += 1
            if j == n - 1:
                count += 1
        return m - count
