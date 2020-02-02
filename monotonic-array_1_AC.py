# https://leetcode.com/problems/monotonic-array/
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        comps = [lambda x, y: x <= y, lambda x, y: x >= y]
        for comp in comps:
            i = 0
            while i < n - 1:
                if not comp(A[i], A[i + 1]):
                    break
                i += 1
            if i == n - 1:
                return True
        return False
