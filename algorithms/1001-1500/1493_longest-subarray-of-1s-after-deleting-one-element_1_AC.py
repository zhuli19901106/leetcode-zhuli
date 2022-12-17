# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        a = nums
        n = len(a)
        tups = []

        i = 0
        f = nums[i]
        while True:
            if f == 0:
                tups.append((f, 1))
                i += 1
            else:
                j = i + 1
                while j < n and a[j] == a[i]:
                    j += 1
                tups.append((f, j - i))
                i = j

            if i == n:
                break
            f = a[i]

        # special case
        nt = len(tups)
        if len(tups) == 1 and tups[0][0] == 1:
            return tups[0][1] - 1

        res = 0
        for i, tp in enumerate(tups):
            x, cc = tp
            if x == 1:
                res = max(res, cc)
                continue

            cur = 0
            if i > 0 and tups[i - 1][0] == 1:
                cur += tups[i - 1][1]
            if i < nt - 1 and tups[i + 1][0] == 1:
                cur += tups[i + 1][1]
            res = max(res, cur)

        return res
