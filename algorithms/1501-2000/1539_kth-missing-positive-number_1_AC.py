# https://leetcode.com/problems/kth-missing-positive-number/
# 1AC, just count it
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        cc = 0
        j = 0
        n = len(arr)
        while cc < k:
            if j >= n or arr[j] > i:
                cc += 1
            else:
                j += 1
            i += 1
        return i - 1
