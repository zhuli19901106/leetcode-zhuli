# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/
# it's not about greedy with a max heap
# binary search

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        a = sorted(nums)

        sm = 0
        n = len(a)
        for x in a:
            sm += x
        if maxOperations >= sm - n:
            return 1

        ll = 1
        rr = a[-1]
        while rr - ll > 1:
            mm = ll + (rr - ll) // 2
            cur = 0

            # count number of ops needed for current search
            for i in range(n - 1, -1, -1):
                if a[i] <= mm:
                    break
                cur += (a[i] + mm - 1) // mm - 1
            if cur > maxOperations:
                ll = mm
            else:
                rr = mm

        return rr
