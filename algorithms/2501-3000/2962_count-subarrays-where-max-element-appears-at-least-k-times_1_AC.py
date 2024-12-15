# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
# sliding window
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        n = len(nums)

        # get k occurrences in a sliding window
        ai = [i for i, x in enumerate(nums) if x == max_val]

        m = len(ai)
        res = 0
        for i in range(0, m - k + 1):
            j = i + k - 1
            ll = ai[i] + 1
            rr = ai[j + 1] - ai[j] if j < m - 1 else n - ai[j]

            res += ll * rr
        return res
