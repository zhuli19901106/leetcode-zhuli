# https://leetcode.com/problems/missing-element-in-sorted-array/
# 1AC, sorted, so a binary search is mandatory
class Solution:
    INT_MAX = 2 ** 31 - 1
    def missingElement(self, nums: List[int], k: int) -> int:
        a = nums
        a.append(Solution.INT_MAX)

        low = 0
        high = len(a) - 1
        while high - low > 1:
            mid = low + (high - low) // 2
            gap = (a[mid] - a[low]) - (mid - low)
            if k > gap:
                low = mid
                k -= gap
            else:
                high = mid
        return a[low] + k
