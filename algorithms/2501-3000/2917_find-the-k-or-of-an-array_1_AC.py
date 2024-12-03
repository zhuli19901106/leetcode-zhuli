# https://leetcode.com/problems/find-the-k-or-of-an-array/
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        res = 0
        b2 = 1

        max_val = max(nums)
        while b2 <= max_val:
            cc = 0
            for x in nums:
                if (x & b2) != 0:
                    cc += 1
            if cc >= k:
                res |= b2
            b2 <<= 1

        return res
