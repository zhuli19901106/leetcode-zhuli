# medium
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
# first intuition is binary search
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        a = nums
        if sum(a) <= threshold:
            return 1

        def check(d, th):
            sum_val = 0
            for x in a:
                sum_val += (x + d - 1) // d
            return sum_val <= th

        low = 1
        high = 2 ** 31 - 1
        while high - low > 1:
            mid = low + (high - low) // 2
            if check(mid, threshold):
                high = mid
            else:
                low = mid
        return high
