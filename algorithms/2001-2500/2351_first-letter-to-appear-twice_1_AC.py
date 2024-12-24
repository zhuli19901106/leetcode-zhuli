# easy
# https://leetcode.com/problems/first-letter-to-appear-twice/
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        st = set()
        for c in s:
            if c in st:
                return c
            else:
                st.add(c)
        return c
