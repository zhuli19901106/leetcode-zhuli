# medium
# https://leetcode.com/problems/prime-subtraction-operation/
# be greedy
from bisect import bisect_left

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        max_val = max(nums)
        p = [True for i in range(max_val + 1)]
        p[0] = p[1] = False

        # sieve of Eratosthenes
        i = 2
        while i <= max_val // i:
            j = i
            while j <= max_val // i:
                p[i * j] = False
                j += 1
            i += 1
        p = [i for i in range(max_val + 1) if p[i]]

        n = len(nums)
        i = 0
        last = 0
        while i < n:
            j = bisect_left(p, nums[i] - last) - 1
            if j == -1:
                # can't subtract any prime
                if nums[i] <= last:
                    return False
                last = nums[i]
            else:
                # can subtract some prime
                last = nums[i] - p[j]
            i += 1

        return True
