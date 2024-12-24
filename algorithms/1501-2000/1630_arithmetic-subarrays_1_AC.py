# medium
# https://leetcode.com/problems/arithmetic-subarrays/
# 1AC, can't think of any elegant solution for better complexity

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        res_cache = {}
        m = len(l)
        for i in range(m):
            ll, rr = l[i], r[i]
            if (ll, rr) in res_cache:
                res.append(res_cache[(ll, rr)])
            arr = nums[ll: rr + 1]
            arr.sort()
            res.append(self.checkArith(arr))
        return res

    def checkArith(self, arr):
        n = len(arr)
        if n <= 2:
            return True
        dt = arr[1] - arr[0]
        for i in range(1, n - 1):
            if arr[i + 1] - arr[i] != dt:
                return False
        return True
