# easy
# https://leetcode.com/problems/find-the-middle-index-in-array/
# 1AC

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)

        pref = [0 for i in range(n)]
        sm = 0
        for i in range(n):
            pref[i] = sm
            sm += nums[i]

        suf = [0 for i in range(n)]
        sm = 0
        for i in range(n - 1, -1, -1):
            suf[i] = sm
            sm += nums[i]

        for i in range(n):
            if pref[i] == suf[i]:
                return i
        return -1
