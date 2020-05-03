# https://leetcode.com/problems/number-of-valid-subarrays/
# 1AC, use a stack
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        a = nums
        n = len(a)

        res = 0
        st = []
        for i, x in enumerate(a):
            while len(st) > 0 and x < st[-1][0]:
                res += i - st[-1][1]
                st.pop()
            st.append((x, i))
        while len(st) > 0:
            res += n - st[-1][1]
            st.pop()
        return res
