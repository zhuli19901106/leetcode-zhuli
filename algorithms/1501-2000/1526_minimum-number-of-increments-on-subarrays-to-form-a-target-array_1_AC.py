# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
# simple, but too slow
# watch the trend

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        last = 0
        for x in target:
            # only necessary when there's a rise in trend
            if x > last:
                res += x - last
            last = x
        return res

    def minNumberOperationsTooSlow(self, target: List[int]) -> int:
        def recurse(a, ll, rr, cur):
            if ll == rr:
                return a[ll] - cur
            min_val = a[ll]
            for i in range(ll + 1, rr + 1):
                if a[i] < min_val:
                    min_val = a[i]
            res = min_val - cur

            i = ll
            while i <= rr:
                while i <= rr and a[i] == min_val:
                    i += 1
                if i > rr:
                    break

                j = i + 1
                while j <= rr and a[j] != min_val:
                    j += 1
                res += recurse(a, i, j - 1, min_val)
                i = j
            return res

        return recurse(target, 0, len(target) - 1, 0)
