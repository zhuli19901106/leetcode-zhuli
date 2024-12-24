# easy
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
# 1AC, brute force
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ps = [0]
        for i in range(n):
            ps.append(ps[-1] + arr[i])
        res = 0
        for i in range(n):
            j = 1
            while i + j <= n:
                res += ps[i + j] - ps[i]
                j += 2
        return res
