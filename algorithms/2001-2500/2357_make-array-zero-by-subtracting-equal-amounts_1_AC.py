# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        st = set(nums)
        if 0 in st:
            st.remove(0)
        return len(st)
