# https://leetcode.com/problems/k-divisible-elements-subarrays/
# for distinct, just use a hash key for each subarray
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        sm = [0]
        n = len(nums)
        for i in range(n):
            sm.append(sm[-1] + (1 if nums[i] % p == 0 else 0))

        res = set()
        for i in range(n):
            key = ''
            for j in range(i, n):
                key += str(nums[j]) + '_'

                if sm[j + 1] - sm[i] <= k:
                    res.add(key)

        return len(res)
