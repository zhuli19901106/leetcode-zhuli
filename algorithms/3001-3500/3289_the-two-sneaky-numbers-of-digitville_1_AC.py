# easy
# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        st = set()
        res = []
        for x in nums:
            if x in st:
                res.append(x)
            st.add(x)
        return res
