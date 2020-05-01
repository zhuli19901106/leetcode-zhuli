# https://leetcode.com/problems/check-if-n-and-its-double-exist/
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        st = set()
        zero = 0
        for x in arr:
            if x == 0:
                zero += 1
            else:
                st.add(x)
        for x in st:
            if 2 * x in st:
                return True
        return zero >= 2
