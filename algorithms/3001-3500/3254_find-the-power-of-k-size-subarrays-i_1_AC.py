# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        cc = [1 for i in range(n)]
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                cc[i] = cc[i - 1] + 1

        res = []
        for i in range(k - 1, n):
            res.append(nums[i] if cc[i] >= k else -1)
        return res
