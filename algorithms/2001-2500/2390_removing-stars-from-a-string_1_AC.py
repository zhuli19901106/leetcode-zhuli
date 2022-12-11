# https://leetcode.com/problems/removing-stars-from-a-string/
class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for c in s:
            if c == '*':
                if len(st) > 0:
                    st.pop()
            else:
                st.append(c)

        return ''.join(st)
