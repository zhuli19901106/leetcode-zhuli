# medium
# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
# this time it's O(n), two pointers

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        a = arr
        n = len(a)

        i = 0
        j = n - 1
        while j > 0 and a[j - 1] <= a[j]:
            j -= 1

        res = j - i
        while i < j:
            while j < n and a[j] < a[i]:
                j += 1

            i += 1
            res = min(res, j - i)

            if i == j or a[i - 1] > a[i]:
                break

        return res
