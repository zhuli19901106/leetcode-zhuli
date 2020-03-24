# https://leetcode.com/problems/confusing-number/
class Solution:
    def confusingNumber(self, N: int) -> bool:
        mm = dict(zip(list('01689'), list('01986')))
        s1 = str(N)
        s2 = ''.join([mm[c] for c in s1[::-1] if c in mm])
        return len(s1) == len(s2) and s1 != s2
