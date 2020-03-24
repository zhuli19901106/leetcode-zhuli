# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        a = sorted(set(nums))
        m = {}
        for x in nums:
            if x in m:
                m[x] += 1
            else:
                m[x] = 1
        n = len(a)
        i = 0
        while i < n:
            j = 0
            val = a[i]
            while j < k:
                if val + j in m and m[val + j] > 0:
                    m[val + j] -= 1
                else:
                    return False
                if m[val + j] == 0:
                    i += 1
                j += 1
        return i == n
