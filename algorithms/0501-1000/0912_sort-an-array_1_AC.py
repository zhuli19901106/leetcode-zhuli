# https://leetcode.com/problems/sort-an-array/
# quick sort by hand
from random import randint

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        a = nums
        n = len(a)
        Solution.qsort(a, 0, n - 1)
        return a

    @staticmethod
    def qsort(a, left, right):
        if left >= right:
            return
        pi = randint(left, right)
        a[pi], a[right] = a[right], a[pi]
        pi = right
        i = left
        j = right - 1
        while True:
            while i <= j and a[i] <= a[pi]:
                i += 1
            while i <= j and a[j] >= a[pi]:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
            else:
                break
        a[i], a[pi] = a[pi], a[i]
        Solution.qsort(a, left, i - 1)
        Solution.qsort(a, i + 1, right)
