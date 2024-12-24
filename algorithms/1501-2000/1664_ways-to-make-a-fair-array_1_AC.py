# medium
# https://leetcode.com/problems/ways-to-make-a-fair-array/
# 1AC, simple idea, but the implementation is a bit cumbersome
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)

        pre = [0 for _ in range(n)]
        odd, even = 0, 0
        for i in range(n):
            if i & 1:
                odd += nums[i]
                pre[i] = odd
            else:
                even += nums[i]
                pre[i] = even
        post = [0 for _ in range(n)]
        odd, even = 0, 0
        for i in range(n - 1, -1, -1):
            if i & 1:
                odd += nums[i]
                post[i] = odd
            else:
                even += nums[i]
                post[i] = even

        res = 0
        for i in range(n):
            if i & 1:
                ed, od = 1, 2
            else:
                ed, od = 2, 1
            e1 = pre[i - ed] if i - ed >= 0 else 0
            o1 = pre[i - od] if i - od >= 0 else 0
            e2 = post[i + ed] if i + ed <= n - 1 else 0
            o2 = post[i + od] if i + od <= n - 1 else 0
            if e1 + o2 == o1 + e2:
                res += 1
        return res
