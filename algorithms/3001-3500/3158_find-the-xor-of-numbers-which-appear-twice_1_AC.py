# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        st = set()
        res = 0
        for x in nums:
            if x in st:
                res ^= x
            st.add(x)
        return res
