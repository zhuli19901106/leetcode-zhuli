# https://leetcode.com/problems/fixed-point/
# binary search
class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        a = A
        n = len(A)
        if a[0] > 0 or a[n - 1] < n - 1:
            return -1
        if a[0] == 0:
            return 0
        low = 0
        high = n - 1
        while high - low > 1:
            mid = low + (high - low) // 2
            if a[mid] < mid:
                low = mid
            else:
                high = mid
        return high if a[high] == high else -1
