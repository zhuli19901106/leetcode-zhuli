# https://leetcode.com/problems/clear-digits/
class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for c in s:
            if c.isalpha():
                st.append(c)
            elif c.isdigit():
                if len(st) > 0:
                    st.pop()
        return ''.join(st)
