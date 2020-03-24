# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# it used to be hard, now it's medium? how time inflates.
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        s = text
        mm = {}
        for c in s:
            if c in mm:
                mm[c] += 1
            else:
                mm[c] = 1
        st = set()
        res = []
        for c in s:
            mm[c] -= 1
            if c in st:
                continue
            while len(res) > 0 and c < res[-1] and mm[res[-1]] > 0:
                st.remove(res.pop())
            res.append(c)
            st.add(c)
        return ''.join(res)
