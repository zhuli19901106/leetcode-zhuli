# medium
# https://leetcode.com/problems/distinct-numbers-in-each-subarray/
# slide and hash

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        mm = {}
        for i in range(k):
            x = nums[i]
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1
        res = [len(mm)]

        n = len(nums)
        for i in range(k, n):
            x, last_x = nums[i], nums[i - k]
            if mm[last_x] <= 1:
                del mm[last_x]
            else:
                mm[last_x] -= 1
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1
            res.append(len(mm))

        return res
