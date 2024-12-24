# easy
# https://leetcode.com/problems/diet-plan-performance/
# 1AC
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        a = calories
        n = len(a)

        sm = 0
        for i in range(k - 1):
            sm += a[i]

        i = k - 1
        last_val = 0
        res = 0
        while i < n:
            sm = sm + a[i] - last_val
            i += 1
            last_val = a[i - k]
            if sm < lower:
                res -= 1
            elif sm > upper:
                res += 1

        return res
