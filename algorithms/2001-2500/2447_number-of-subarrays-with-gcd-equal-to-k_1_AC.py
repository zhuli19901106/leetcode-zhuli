# https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/
# for this size it's OK to BF
# can't think of any O(n) or O(nlogn) methods for now
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            g = nums[i]
            if g == k:
                res += 1
            for j in range(i + 1, n):
                g = self.gcd(g, nums[j])
                if g == k:
                    res += 1
        return res

    def gcd(self, x, y):
        while y != 0:
            x, y = y, x % y
        return x
