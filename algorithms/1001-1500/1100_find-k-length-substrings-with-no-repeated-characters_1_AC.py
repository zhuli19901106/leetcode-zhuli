# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/
# 1AC, fixed sliding window
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        s = S
        k = K
        if len(s) < k:
            return 0
        mm = {}
        i = 0
        uc = 0
        while i < k:
            if s[i] in mm:
                mm[s[i]] += 1
            else:
                mm[s[i]] = 1
                uc += 1
            i += 1

        res = 0
        if uc == k:
            res += 1
        n = len(s)

        while i < n:
            if s[i] in mm:
                mm[s[i]] += 1
            else:
                mm[s[i]] = 1
                uc += 1

            if mm[s[i - k]] > 1:
                mm[s[i - k]] -= 1
            else:
                del mm[s[i - k]]
                uc -= 1
            if uc == k:
                res += 1
            i += 1

        return res
