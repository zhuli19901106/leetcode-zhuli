# easy
# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        i, j = 0, 0
        cc = [0, 0]

        res = 0
        a = [ord(c) - ord('0') for c in s]
        n = len(s)
        while j < n:
            cc[a[j]] += 1

            while i < j and (cc[0] > k and cc[1] > k):
                cc[a[i]] -= 1
                i += 1
            res += j - i + 1
            j += 1
        return res
