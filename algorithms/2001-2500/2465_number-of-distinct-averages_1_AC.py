# https://leetcode.com/problems/number-of-distinct-averages/
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        st = set()
        a = sorted(nums)
        n = len(a)
        i1, i2 = 0, n - 1
        while i1 <= i2:
            st.add(a[i1] + a[i2])
            i1 += 1
            i2 -= 1
        return len(st)
