# https://leetcode.com/problems/count-vowel-substrings-of-a-string/
# 1AC, bit op

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def mask(s):
            res = 0
            for c in s:
                res |= (1 << ord(c) - ord('a'))
            return res

        m0 = mask('aeiou')
        st0 = set(list('aeiou'))

        res = 0
        n = len(word)
        for i in range(n):
            m = 0
            for j in range(i, n):
                m |= mask(word[j])
                if (m & m0) != m:
                    break
                if m == m0:
                    res += 1
        return res
