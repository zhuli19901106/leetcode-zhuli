# https://leetcode.com/problems/maximum-prime-difference/
# should be easy
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        n = len(nums)

        i1 = 0
        while i1 < n and not self.isPrime(nums[i1]):
            i1 += 1
        i2 = n - 1
        while i2 > -1 and not self.isPrime(nums[i2]):
            i2 -= 1
        return i2 - i1

    def isPrime(self, x):
        if x < 2:
            return False

        i = 2
        while i <= x // i:
            if x % i == 0:
                return False
            i += 1
        return True
