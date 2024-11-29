# https://leetcode.com/problems/prime-in-diagonal/
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            x = nums[i][i]
            if self.isPrime(x) and x > res:
                res = x
            x = nums[i][n - 1 - i]
            if self.isPrime(x) and x > res:
                res = x
        return res

    def isPrime(self, x):
        if x < 2:
            return False
        i = 2
        while i <= x // i:
            if x % i == 0:
                return False
            i += 1
        return True
