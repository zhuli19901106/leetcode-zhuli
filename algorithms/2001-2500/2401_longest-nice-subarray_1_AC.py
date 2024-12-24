# medium
# https://leetcode.com/problems/longest-nice-subarray/
# all the same except for add/remove using bit operations
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        res = 1
        j = 0
        mm = {}
        for i in range(n):
            while self.checkBits(nums[i], mm):
                self.removeBits(nums[j], mm)
                j += 1
            res = max(res, i - j + 1)
            self.addBits(nums[i], mm)
        return res

    def checkBits(self, x, mm):
        while x != 0:
            b = (x & -x)
            if b in mm and mm[b] > 0:
                return True
                break
            else:
                x ^= b

        return False

    def addBits(self, x, mm):
        while x != 0:
            b = (x & -x)
            if not b in mm:
                mm[b] = 0
            mm[b] += 1
            x ^= b

    def removeBits(self, x, mm):
        while x != 0:
            b = (x & -x)
            mm[b] -= 1
            if mm[b] == 0:
                del mm[b]
            x ^= b
