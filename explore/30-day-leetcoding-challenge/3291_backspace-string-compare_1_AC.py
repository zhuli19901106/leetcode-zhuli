# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3291/
# 1AC
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def process(s):
            st = []
            for c in s:
                if c == '#':
                    if len(st) > 0:
                        st.pop()
                else:
                    st.append(c)
            return ''.join(st)

        return process(S) == process(T)
