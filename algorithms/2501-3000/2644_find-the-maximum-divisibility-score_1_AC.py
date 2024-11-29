# https://leetcode.com/problems/find-the-maximum-divisibility-score/
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_cc, min_val = 0, divisors[0]
        nn, nd = len(nums), len(divisors)
        for i in range(nd):
            cc = 0
            for j in range(nn):
                if nums[j] % divisors[i] == 0:
                    cc += 1
            if cc > max_cc or (cc == max_cc and divisors[i] < min_val):
                max_cc, min_val = cc, divisors[i]
        return min_val
