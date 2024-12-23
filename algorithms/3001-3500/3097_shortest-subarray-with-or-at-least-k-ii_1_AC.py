# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        sm = 0
        mm = {}

        res = -1
        j = 0
        for i, x in enumerate(nums):
            while x != 0:
                b = (x & -x)
                mm[b] = mm.get(b, 0) + 1
                x ^= b

                if mm[b] == 1:
                    sm ^= b
            if sm < k:
                continue

            while j <= i and sm >= k:
                y = nums[j]
                while y != 0:
                    b = (y & -y)
                    mm[b] -= 1
                    y ^= b

                    if mm[b] == 0:
                        sm ^= b
                j += 1
            if res == -1 or res > i - j + 2:
                res = i - j + 2

        return res
