# easy
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
# O(n)
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for i, val in enumerate(arr):
            x, y = i + 1, n - i
            cc = (x // 2) * (y // 2) + ((x + 1) // 2) * ((y + 1) // 2)
            res += cc * val
        return res
