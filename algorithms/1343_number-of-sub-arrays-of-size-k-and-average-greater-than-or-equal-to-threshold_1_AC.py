# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
# what kind of medium is this?
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        a = arr
        n = len(a)
        res = 0
        s = 0
        for i in range(k):
            s += a[i]
        if s >= k * threshold:
            res += 1

        for i in range(k, n):
            s += (a[i] - a[i - k])
            if s >= k * threshold:
                res += 1
        return res
