# medium
# https://leetcode.com/problems/maximum-erasure-value/
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        a = nums
        n = len(a)

        st = set()
        res = 0
        cur = 0
        i, j = 0, 0
        while i < n:
            while j < n and not a[j] in st:
                st.add(a[j])
                cur += a[j]
                j += 1
                res = max(res, cur)
            if j == n:
                break
            while i < j and a[j] in st:
                st.remove(a[i])
                cur -= a[i]
                i += 1

        return res
