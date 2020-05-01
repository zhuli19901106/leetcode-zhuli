# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3304/
# 1AC
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = nums
        n = len(a)
        if n == 0:
            return -1
        if n == 1:
            return 0 if a[0] == target else -1
        idx = self.findFirst(a)
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            val = a[(mid + idx) % n]
            if target < val:
                high = mid - 1
            elif target > val:
                low = mid + 1
            else:
                return (mid + idx) % n
        return -1

    def findFirst(self, a):
        n = len(a)
        if a[0] < a[-1]:
            return 0
        low = 0
        high = n - 1
        while low + 1 < high:
            mid = low + (high - low) // 2
            if a[mid] > a[high]:
                low = mid
            else:
                high = mid
        return high
