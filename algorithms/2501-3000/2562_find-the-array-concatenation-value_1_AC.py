# https://leetcode.com/problems/find-the-array-concatenation-value/
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        sm = 0

        i, j = 0, n - 1
        while i < j:
            cc = 0
            x = nums[j]
            while x != 0:
                x //= 10
                cc += 1
            sm += nums[i] * 10 ** cc + nums[j]
            i += 1
            j -= 1
        if i == j:
            sm += nums[i]

        return sm
