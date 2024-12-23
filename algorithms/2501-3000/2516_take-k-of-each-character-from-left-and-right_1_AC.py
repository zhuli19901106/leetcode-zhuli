# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/
# a variant of two pointers
# took me over 10 minutes to get it
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        abc = 'abc'
        mm = {}
        for c in abc:
            mm[c] = 0

        n = len(s)
        for i in range(n):
            mm[s[i]] += 1

        for c in abc:
            if mm[c] < k:
                return -1

        res = n
        j = n
        for i in range(n - 1, -1, -1):
            c = s[i]
            mm[c] -= 1

            while mm[c] < k:
                j -= 1
                mm[s[j]] += 1

            cur = i + n - j
            res = min(res, cur)
        return res
