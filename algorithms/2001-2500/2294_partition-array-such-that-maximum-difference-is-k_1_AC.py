# medium
# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        a = sorted(nums)
        n = len(a)

        res = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and a[j] - a[i] <= k:
                j += 1
            res += 1
            i = j

        return res
