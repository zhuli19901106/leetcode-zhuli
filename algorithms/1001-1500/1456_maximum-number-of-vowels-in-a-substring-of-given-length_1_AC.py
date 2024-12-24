# medium
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0

        st_vow = set(list('aeiou'))
        mm = {}
        cc = 0
        n = len(s)
        for i in range(k):
            c = s[i]
            if not c in st_vow:
                continue
            if c in mm:
                mm[c] += 1
            else:
                mm[c] = 1
            cc += 1
        res = max(res, cc)

        i = k
        while i < n:
            c = s[i]
            if c in st_vow:
                if c in mm:
                    mm[c] += 1
                else:
                    mm[c] = 1
                cc += 1

            c1 = s[i - k]
            if c1 in st_vow:
                if mm[c1] == 1:
                    del mm[c1]
                else:
                    mm[c1] -= 1
                cc -= 1

            res = max(res, cc)
            i += 1

        return res
