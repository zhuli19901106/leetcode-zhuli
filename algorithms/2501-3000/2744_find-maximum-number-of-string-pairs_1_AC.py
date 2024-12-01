# https://leetcode.com/problems/find-maximum-number-of-string-pairs/
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        st = set()
        res = 0
        for w in words:
            rw = w[::-1]
            if w == rw:
                continue

            if rw in st:
                res += 1
            st.add(w)

        return res
