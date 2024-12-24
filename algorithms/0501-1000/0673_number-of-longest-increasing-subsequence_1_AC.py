# medium
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# simple idea, heavy work
from bisect import bisect_left

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        a = nums
        n = len(a)
        if n == 0:
            return 0

        dp = [1 for i in range(n)]

        seq = [a[0]]
        max_len = 1
        for i in range(1, n):
            if a[i] > seq[-1]:
                seq.append(a[i])
                dp[i] = len(seq)
            else:
                j = bisect_left(seq, a[i])
                seq[j] = a[i]
                dp[i] = j + 1
            max_len = max(max_len, dp[i])
        
        mm = [{} for i in range(max_len + 1)]
        for i in range(n):
            if dp[i] == 1:
                mm[dp[i]][i] = 1
            else:
                val = 0
                for j, cc in mm[dp[i] - 1].items():
                    if a[j] >= a[i]:
                        continue
                    val += cc
                mm[dp[i]][i] = val
        res = sum(mm[max_len].values())
        return res
