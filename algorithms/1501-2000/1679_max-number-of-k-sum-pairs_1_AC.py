# medium
# https://leetcode.com/problems/max-number-of-k-sum-pairs/
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        a = sorted(nums)
        n = len(a)
        i, j = 0, n - 1
        res = 0
        while i < j:
            val = a[i] + a[j]
            if val < k:
                i += 1
            elif val > k:
                j -= 1
            else:
                i += 1
                j -= 1
                res += 1

        return res
