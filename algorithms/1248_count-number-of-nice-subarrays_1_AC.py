# https://leetcode.com/problems/count-number-of-nice-subarrays/
# hash and count
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        a = nums
        n = len(a)
        m = {0: 1}
        cnt = 0
        for i in range(n):
            if a[i] % 2 == 1:
                cnt += 1
            if cnt in m:
                m[cnt] += 1
            else:
                m[cnt] = 1
        res = 0
        for x in m:
            if x - k in m:
                res += m[x] * m[x - k]
        return res
