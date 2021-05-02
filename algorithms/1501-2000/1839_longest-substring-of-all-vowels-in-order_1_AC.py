# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/
# no hurry
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        s = word
        n = len(s)
        st = set()

        res = 0
        i = 0
        while i < n:
            st.clear()
            st.add(s[i])
            j = i + 1
            while j < n and s[j] >= s[j - 1]:
                st.add(s[j])
                j += 1
            if len(st) == 5:
                res = max(res, j - i)
            i = j
        return res
