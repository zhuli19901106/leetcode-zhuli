# medium
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        INT_MAX = -(2 ** 31)

        a = A
        a.sort()
        st = set()
        max_val = INT_MAX
        res = 0
        for x in a:
            if not x in st:
                max_val = x
            else:
                max_val += 1
                res += max_val - x
            st.add(max_val)
        return res
