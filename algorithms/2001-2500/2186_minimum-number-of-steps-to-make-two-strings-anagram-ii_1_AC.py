# medium
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        def countChars(s):
            mm = {}
            for c in s:
                if c in mm:
                    mm[c] += 1
                else:
                    mm[c] = 1
            return mm

        ms = countChars(s)
        mt = countChars(t)
        st = set()
        for c in ms:
            st.add(c)
        for c in mt:
            st.add(c)

        res = 0
        for c in st:
            if not c in ms:
                res += mt[c]
                continue
            if not c in mt:
                res += ms[c]
                continue
            res += abs(ms[c] - mt[c])

        return res
