# easy
# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
# 1AC
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                i += 1
                continue
            j = i + 1
            while j < n and nums[j] == 0:
                j += 1
            if j == n:
                break
            if j - i <= k:
                return False
            i = j
        return True
